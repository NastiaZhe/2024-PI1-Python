cislo = int(input("Zadaj čislo: "))
# vypis parnych cisiel
print(f"Párne čísla do {cislo}: ")
for i in range(2, cislo+1, 2):
    print(i)
# vypis neparnych cisiel
print(f"Nepárne čísla do {cislo}: ")
for i in range(1, cislo+1, 2):
    print(i)
if cislo % 2 == 0: 
    print(f"čislo {cislo} je parne")
else:
    print(f"čislo {cislo} je neparne")