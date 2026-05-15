program = [
    "MACRO INCR &P1,&P2",
    "LDA &P1",
    "ADD &P2",
    "STA &P1",
    "MEND",

    "MACRO SUBR &A,&B",
    "LDA &A",
    "SUB &B",
    "STA &A",
    "MEND",

    "START",
    "INCR A,B",
    "SUBR X,Y",
    "END",
]

NAMETAB = []
DEFTAB = []

i = 0
while i < len(program):
    line = program[i]
    if line.startswith("MACRO"):
        parts = line.split()
        macro_name = parts[1]
        start_index = len(DEFTAB)
        DEFTAB.append(line)
        i += 1
        while program[i] != "MEND":
            DEFTAB.append(program[i])
            i += 1
        DEFTAB.append("MEND")
        end_index = len(DEFTAB) - 1
        NAMETAB.append([macro_name, start_index, end_index])
    i += 1

print("NAMETAB:")
print(f"{'MACRO NAME':<15}{'START':<10}{'END'}")
for row in NAMETAB:
    print(f"{row[0]:<15}{row[1]:<10}{row[2]}")

print("\nDEFTAB:")
print(f"{'INDEX':<10}{'DEFINITION'}")
for i in range(len(DEFTAB)):
    print(f"{i:<10}{DEFTAB[i]}")
