program = [

    "PG1 START 0000",
    "EXTDEF A, B",
    "EXTREF C, D",
    "ADD ABC",
    "A SUB PQR",
    "ADD ABC1",
    "B MUL ABC",
    "END"
]

location_counter = 0
extdef = []
extref = []
symbol_table = {}

for line in program:
  words = line.replace(",", "").split()
  if "START" in line:
    location_counter = int(words[2], 16)
  elif words[0] == "EXTDEF":
    extdef = words[1:]
  elif words[0] == "EXTREF":
    extref = words[1:]
  elif words[0] == "END":
    break
  else:
    if len(words) == 3:
      label = words[0]
      symbol_table[label] = \
          hex(location_counter)[2:].zfill(6).upper()
    location_counter += 3

d_record = "D"
for symbol in extdef:
  if symbol in symbol_table:
    d_record += "^" + symbol + "^" + symbol_table[symbol]

r_record = "R"
for symbol in extref:
  r_record += "^" + symbol

print("\nD RECORD\n")
print(d_record)
print("\nR RECORD\n")
print(r_record)
print("\nLocal Symbol Table\n")
print("Symbol Name\tValue")
for symbol in symbol_table:
  print(symbol, "\t\t", symbol_table[symbol])