stack = []
operators = ["+", "-", "*", "/", "="]
precedence = {"=": 0, "+": 1, "-": 1, "*": 2, "/": 2}

def infix_to_postfix(expression):
    output = []
    op_stack = []
    for ch in expression:
        if ch.isalnum():
            output.append(ch)
        elif ch == "(":
            op_stack.append(ch)
        elif ch == ")":
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()
        else:
            while (
                op_stack
                and op_stack[-1] != "("
                and precedence[op_stack[-1]] >= precedence[ch]
            ):
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

print("\nQuadruple Representation:")
print(f"{'OPERATOR':<12}{'ARG1':<12}{'ARG2':<12}{'RESULT'}")

for row in quadruple:
    print(f"{row[0]:<12}{row[1]:<12}{row[2]:<12}{row[3]}")

print("\nTriple Representation:")
print(f"{'INDEX':<10}{'OPERATOR':<12}{'ARG1':<10}{'ARG2'}")

for i in range(len(triple)):
    row = triple[i]
    print(f"{i:<10}{row[0]:<12}{row[1]:<10}{row[2]}")
