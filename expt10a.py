program = [
    "START 1000",

    "USE CODE",
    "LDA ALPHA",
    "STA BETA",

    "USE DATA",
    "RESW 2",

    "USE EXTRA",
    "LDA GAMMA",

    "END",
]

blocks = {}
current_block = "DEFAULT"
start_address = 0x1000

for line in program:
    words = line.split()
    if words[0] == "START":
        start_address = int(words[1], 16)
    elif words[0] == "USE":
        current_block = words[1]
        if current_block not in blocks:
            blocks[current_block] = 0
    elif words[0] == "END":
        break
    else:
        if current_block not in blocks:
            blocks[current_block] = 0
        if words[0] == "RESW":
            blocks[current_block] += int(words[1]) * 3
        else:
            blocks[current_block] += 3

print("PROGRAM BLOCK TABLE:")
print(f"{'BLOCK':<15}{'START ADDRESS':<20}{'LENGTH'}")
address = start_address
for block in blocks:
    print(f"{block:<15}{hex(address)[2:].upper():<20}{blocks[block]}")
    address += blocks[block]
