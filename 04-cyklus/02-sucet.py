n = int(input("Zadaj n: "))
sucet = 0
for i in range(n):
    sucet = sucet + (i+1) # sucet + (i+1) je výraz, najskôr vypočíta výraz a výsledná hodnota sa priradí do premennej sucet
    # print(i, i+1, sucet)
print("Súčet prvých", n, "čísel je", sucet)    

