table = {
  ('E', 'i') : 'TA',
  ('E', '(') : 'TA', 

  ('A', '+') : '+TA',
  ('A', ')') : 'e',
  ('A', '$') : 'e',
 
  ('T', 'i') : 'FB',
  ('T', '(') : 'FB',
 
  ('B', '*') : '*FB',
  ('B', '+') : 'e',
  ('B', ')') : 'e',
  ('B', '$') : 'e',
 
  ('F', 'i') : 'i',
  ('F', '(') : '(E)'
}

def isNonTerminal(ch):
  return ch.isupper()

print('Grammar used: ')
print('E->TA')
print('A->+TA|e')
print('T->FB')
print('B->*FB|e')
print('B->(E)|i')

input_str = input("Enter input string: ")
if input_str[-1] != '$':
  input_str += '$'

stack = []
stack.append('$')
stack.append('E')
pointer = 0

print('STACK\t\tINPUT\t\tACTION')

while len(stack) > 0:
  top = stack[-1]
  curr = input_str[pointer]
  stack_str = "".join(stack)
  remaining_input = input_str[pointer:]
  if top == curr:
    print(stack_str, '\t\t', remaining_input, '\t\t Match', curr)
    stack.pop()
    pointer += 1
    
    if top == '$':
      print('\nSTRING ACCEPTED')
      break
  elif isNonTerminal(top):
    key = (top, curr)
    if key in table:
      production = table[key]
      print(stack_str,'\t\t', remaining_input, '\t\t', top, '->', production)
      stack.pop()
      if production != 'e':
        for symbol in reversed(production):
          stack.append(symbol)
    else:
      print(stack_str, '\t\t', remaining_input, '\t\terror')
      print('STRING REJECTED')
      break
  else:
    print(stack_str, '\t\t', remaining_input, '\t\terror')
    print('STRING REJECTED')
    break