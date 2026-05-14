action = {
  (0, 'c'): 'S3',
  (0, 'd'): 'S4',

  (1, '$'): 'ACC',

  (2, 'c'): 'S3',
  (2, 'd'): 'S4',

  (3, 'c'): 'S3',
  (3, 'd'): 'S4',

  (4, 'c'): 'R3',
  (4, 'd'): 'R3',
  (4, '$'): 'R3',

  (5, '$'): 'R1',

  (6, 'c'): 'R2',
  (6, 'd'): 'R2',
  (6, '$'): 'R2'
}

goto = {
  (0, 'S'): 1,
  (0, 'C'): 2,

  (2, 'C'): 5,

  (3, 'C'): 6
}

productions = {
  1: ('S', 'CC'),
  2: ('C', 'cC'),
  3: ('C', 'd')
}

input_string = input("Enter input string: ")

if input_string[-1] != '$':
    input_string += '$'

stack = [0]
pointer = 0
print("STACK\t\tINPUT\t\tACTION")

while True:
    state = stack[-1]
    curr = input_string[pointer]
    stack_str = " ".join(map(str, stack))
    remaining = input_string[pointer:]

    if (state, curr) not in action:
        print(stack_str, "\t", remaining, "\tERROR")
        print("\nSTRING REJECTED")
        break

    act = action[(state, curr)]
    if act[0] == 'S':
        next_state = int(act[1:])
        print(stack_str, "\t", remaining, "\tSHIFT", next_state)
        stack.append(curr)
        stack.append(next_state)
        pointer += 1

    elif act[0] == 'R':
        prod_num = int(act[1:])
        left, right = productions[prod_num]
        print(stack_str, "\t", remaining, "\tREDUCE", left, "->", right)
        pop_length = len(right) * 2

        for i in range(pop_length):
            stack.pop()

        top_state = stack[-1]
        stack.append(left)
        stack.append(goto[(top_state, left)])

    elif act == 'ACC':
        print(stack_str, "\t", remaining, "\tACCEPT")
        print("\nSTRING ACCEPTED")
        break