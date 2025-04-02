import random

teploty = []
pocet_dni = 30

# naplní list teploty náhodnými teplotymi z rozsahu od 10 do 30
for i in range(pocet_dni):
    # teploty[i] = random.randint() vráti chybu, lebo prvky ešte neexistujú
    teploty.append(random.randint(10, 30))

# vypíše list teploty
for i in range(pocet_dni):
    print(f"{i+1}.deň - {teploty[i]}°C")

# vypočíta a vypíše priemernú teplotu
# priemerna_teplota = sum(teploty) / pocet_dni
# print(priemerna_teplota)
suma = 0
for i in range(pocet_dni): 
    suma += teploty[i] # suma = suma + teploty[i]
priemerna_teplota = suma / pocet_dni
print(f"Priemerná teplota v mesiaci je {priemerna_teplota:.2f}°C") # :.2f naformátuje vystup float na dve desatinné miesta

print("Dni s podpriemernou teplotou")
for i in range(pocet_dni):
   if teploty[i] < priemerna_teplota:
      print(f"{i+1}.deň - {teploty[i]}°C") 
