stack = []
operators = ['+', '-', '*', '/', '=']
precedence = {
    '=': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def infix_to_postfix(expression):
  output = []
  op_stack = []
  for ch in expression:
    if ch.isalnum():
      output.append(ch)
    elif ch == '(':
      op_stack.append(ch)
    elif ch == ')':
      while op_stack and op_stack[-1] != '(':
        output.append(op_stack.pop())
      op_stack.pop()
    else:
      while (op_stack and op_stack[-1] != '(' and precedence[op_stack[-1]] >= precedence[ch]):
        output.append(op_stack.pop())
      op_stack.append(ch)

  while op_stack:
      output.append(op_stack.pop())
  return output

choice = input("Enter expression type (infix/postfix): ")
if choice == "infix":
  expr = input("Enter infix expression: ")
  postfix = infix_to_postfix(expr)

else:
  postfix = input("Enter postfix expression: ").split()

if isinstance(postfix, list) == False:
  postfix = list(postfix)

print("\nPostfix Expression:")
print(" ".join(postfix))

temp_count = 1
quadruple = []
triple = []
for symbol in postfix:
  if symbol not in operators:
    stack.append(symbol)
  else:
    operand2 = stack.pop()
    operand1 = stack.pop()
    temp = "T" + str(temp_count)
    quadruple.append([symbol, operand1, operand2, temp])
    op1 = operand1
    op2 = operand2
    if operand1.startswith("T"):
      op1 = "(" + str(int(operand1[1:]) - 1) + ")"

    if operand2.startswith("T"):
      op2 = "(" + str(int(operand2[1:]) - 1) + ")"

    triple.append([symbol, op1, op2])
    stack.append(temp)
    temp_count += 1

print("\nQuadruple Representation:\n")
print("Operator\tArg1\tArg2\tResult")

for row in quadruple:
  print(row[0],"\t\t", row[1], "\t", row[2], "\t",row[3])

print("\nTriple Representation:\n")
print("Index\tOperator\tArg1\tArg2")

for i in range(len(triple)):
  row = triple[i]
  print(i, "\t", row[0], "\t\t", row[1], "\t", row[2])