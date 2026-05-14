keywords = ["if", "else", "while", "for", "int", "switch"]
operators = ["+", "-", "*", "/", "=", ">", "<"]

code = """
int count = 10
if count > 5
count = count + 1
2temp
110.2
abc
"""

code += " "
state = 0
token = ""

print(f"{'TOKEN':<15}{'TYPE'}")
for ch in code:
    if state == 0:
        if ch.isalpha() or ch == "_":
            token += ch
            state = 1
        elif ch.isdigit():
            token += ch
            state = 2
        elif ch in operators:
            print(f"{ch:<15}OPERATOR")
        elif ch in [" ", "\n", "\t"]:
            continue
        else:
            print(f"{ch:<15}INVALID")

    elif state == 1:
        if ch.isalnum() or ch == "_":
            token += ch
        else:
            if token in keywords:
                print(f"{token:<15}KEYWORD")
            else:
                print(f"{token:<15}IDENTIFIER")
            token = ""
            state = 0
            if ch not in [" ", "\n", "\t"] and ch in operators:
                print(f"{ch:<15}OPERATOR")

    elif state == 2:
        if ch.isdigit():
            token += ch
        elif ch == ".":
            token += ch
            state = 3
        elif ch.isalpha() or ch == "_":
            token += ch
            state = 4
        else:
            print(f"{token:<15}INTEGER")
            token = ""
            state = 0
            if ch not in [" ", "\n", "\t"] and ch in operators:
                print(f"{ch:<15}OPERATOR")

    elif state == 3:
        if ch.isdigit():
            token += ch
        else:
            print(f"{token:<15}FLOAT")
            token = ""
            state = 0
            if ch not in [" ", "\n", "\t"] and ch in operators:
                print(f"{ch:<15}OPERATOR")

    elif state == 4:
        if ch.isalnum() or ch == "_":
            token += ch
        else:
            print(f"{token:<15}INVALID IDENTIFIER")
            token = ""
            state = 0
