grammar = {}
n = int(input("Enter number of productions: "))
print("Enter productions")

for i in range(n):
  rule = input()
  left, right = rule.split('->')
  grammar[left] = right.split('|')

def tokenize(prod):
  tokens = []
  i = 0
  while i < len(prod):
    if i + 1 < len(prod) and prod[i + 1] == "'":
      tokens.append(prod[i] + "'")
      i += 2
    else:
      tokens.append(prod[i])
      i += 1
  return tokens

new_grammar = {}

for nt in grammar:
  alpha = []
  beta = []
  for prod in grammar[nt]:
    tokens = tokenize(prod)
    if tokens[0] == nt:
      alpha.append(tokens[1:])
    else:
      beta.append(tokens)
  if alpha:
    new_nt = nt + "'"
    new_grammar[nt] = []
    for b in beta:
      new_grammar[nt].append(b + [new_nt])
    new_grammar[new_nt] = []
    for a in alpha:
      new_grammar[new_nt].append(a + [new_nt])
    new_grammar[new_nt].append(['e'])
  else:
    new_grammar[nt] = [tokenize(p) for p in grammar[nt]]

print("\nGrammar after removing left recursion:\n")
for nt in new_grammar:
  rhs = []
  for prod in new_grammar[nt]:
    rhs.append("".join(prod))
  print(nt, '->', ' | '.join(rhs))


first = {}
for nt in new_grammar:
  first[nt] = set()
  for prod in new_grammar[nt]:
    first[nt].add(prod[0])


print('\nFIRST\n')
for nt in first:
  print(nt, ": ", first[nt])

follow = {}

for nt in new_grammar:
  follow[nt] = set()

start = list(new_grammar.keys())[0]
follow[start].add('$')


for head in new_grammar:
  for prod in new_grammar[head]:
    for i in range(len(prod)):
      symbol = prod[i]
      if symbol in new_grammar:
        if i + 1 < len(prod):
          next_symbol = prod[i + 1]
          if next_symbol in first:
            follow[symbol].update(first[next_symbol] - {'e'})
          else:
            follow[symbol].add(next_symbol)
        else:
          follow[symbol].update(follow[head])

print('\nFOLLOW\n')
for nt in follow:
  print(nt, ": ", follow[nt])