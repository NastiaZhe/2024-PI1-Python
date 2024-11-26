cislo = int(input("Zadaj čislo:"))
print(f"Parne čisla do {cislo}:")
for i in range(2, cislo+1, 2):
    print(i)
print(f"Neparne čisla do {cislo}:")
for i in range(1, cislo+1, 2):
    print(i)
if cislo % 2 == 0:
    print(f"Čislo {cislo} parne")
else:
    print(f"Čislo {cislo} neparne")
