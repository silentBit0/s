table = {
    ("E", "i"): "TA",
    ("E", "("): "TA",

    ("A", "+"): "+TA",
    ("A", ")"): "e",
    ("A", "$"): "e",

    ("T", "i"): "FB",
    ("T", "("): "FB",

    ("B", "*"): "*FB",
    ("B", "+"): "e",
    ("B", ")"): "e",
    ("B", "$"): "e",

    ("F", "i"): "i",
    ("F", "("): "(E)",
}

def is_non_terminal(ch):
    return ch.isupper()

print("Grammar used: ")
print("E->TA")
print("A->+TA|e")
print("T->FB")
print("B->*FB|e")
print("B->(E)|i")

input_str = input("\nEnter input string: ")
if input_str[-1] != "$":
    input_str += "$"

stack = []
stack.append("$")
stack.append("E")
pointer = 0

print(f"\n{'STACK':<20}{'INPUT':<20}{'ACTION'}")

while len(stack) > 0:
    top = stack[-1]
    curr = input_str[pointer]
    stack_str = "".join(stack)
    remaining_input = input_str[pointer:]

    if top == curr:
        print(f"{stack_str:<20}{remaining_input:<20}Match {curr}")
        stack.pop()
        pointer += 1

        if top == "$":
            print("\nSTRING ACCEPTED")
            break

    elif is_non_terminal(top):
        key = (top, curr)
        if key in table:
            production = table[key]
            print(f"{stack_str:<20}{remaining_input:<20}{top} -> {production}")
            stack.pop()
            if production != "e":
                for symbol in reversed(production):
                    stack.append(symbol)

        else:
            print(f"{stack_str:<20}{remaining_input:<20}ERROR")
            print("STRING REJECTED")
            break

    else:
        print(f"{stack_str:<20}{remaining_input:<20}ERROR")
        print("STRING REJECTED")
        break
