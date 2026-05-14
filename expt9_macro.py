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
  "END"
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

print("\nNAMETAB\n")
print("Macro Name\tStart\tEnd")
for row in NAMETAB:
  print(row[0], "\t\t", row[1], "\t", row[2])

print("\nDEFTAB\n")
for i in range(len(DEFTAB)):
  print(i, "\t", DEFTAB[i])