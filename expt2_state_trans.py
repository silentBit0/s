keywords = ["if", "else", "while", "for", "int", "switch"]
operators = ['+', '-', '*', '/', '=', '>', '<']


code = '''
int count = 10
if count > 5
count = count + 1
'''

code += " "
state = 0
token = ""

print("TOKEN\t\tTYPE\n")
for ch in code:
  if state == 0:
    if ch.isalpha() or ch == "_":
        token += ch
        state = 1
    elif ch.isdigit():
        token += ch
        state = 2
    elif ch in operators:
        print(ch, "\t\tOPERATOR")
    elif ch in [' ', '\n', '\t']:
        continue
    else:
        print(ch, "\t\tINVALID")

  elif state == 1:
    if ch.isalnum() or ch == "_":
        token += ch
    else:
        if token in keywords:
            print(token, "\t\tKEYWORD")
        else:
            print(token, "\t\tIDENTIFIER")
        token = ""
        state = 0
        if ch not in [' ', '\n', '\t']:
            if ch in operators:
                print(ch, "\t\tOPERATOR")

  elif state == 2:
    if ch.isdigit():
      token += ch
    else:
        print(token, "\t\tINTEGER")
        token = ""
        state = 0
        if ch not in [' ', '\n', '\t']:
            if ch in operators:
                print(ch, "\t\tOPERATOR")