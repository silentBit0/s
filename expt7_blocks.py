n = int(input("Enter number of TAC instructions: "))
tac = []

print("Enter Three Address Code:")

for i in range(n):
    tac.append(input())

leaders = [1]

for i in range(n):
    if "goto" in tac[i]:
        words = tac[i].split()
        target = words[-1]
        target = target.replace("(", "")
        target = target.replace(")", "")
        target = int(target)
        leaders.append(target)
        if i + 2 <= n:
            leaders.append(i + 2)

leaders = sorted(set(leaders))

print("\nBasic Blocks:")
for i in range(len(leaders)):
    start = leaders[i]
    if i + 1 < len(leaders):
        end = leaders[i + 1] - 1
    else:
        end = n
    print("B" + str(i + 1), ": Starts =", start, ", Ends =", end)

block_map = {}
for i in range(len(leaders)):
    block_map[leaders[i]] = "B" + str(i + 1)

print("\nFlow Graph:")
for i in range(len(leaders)):
    start = leaders[i]
    if i + 1 < len(leaders):
        end = leaders[i + 1] - 1
    else:
        end = n
    print("\nB" + str(i + 1) + ":")
    for j in range(start - 1, end):
        line = tac[j]
        if "goto" in line:
            words = line.split()
            target = words[-1]
            target = target.replace("(", "")
            target = target.replace(")", "")
            target = int(target)
            block_name = block_map[target]
            line = line.replace(words[-1], block_name)
        print(line)
