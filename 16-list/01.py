teploty = [10, 13, 15, 20]
print(teploty)
print(teploty[0])

nakup = ["chlieb", "maslo", "mlieko"]
print(nakup)
print(nakup[1])

zviera = ["pes", "Dunčo", 2020, "hnedá", 10.7] # do listu môžeme ukladať hodnoty rôznych typov (int, str, bool, ...)
print(zviera)
print(zviera[2])

# v Phythone sú listy dynamické, to znamená, že nemusia mať definovanú veľkosť (počet prvkov)
# prvky pridávame pomocou funkcie append()
prazdny = []
print(prazdny)
prazdny.append(25)
print(prazdny)
prazdny.append("Ahoj")
print(prazdny)
prazdny.append(100)
print(prazdny)
print(prazdny[-1])

# listy vieme aj zreťaziť (spočítať)
nakupyazvierata = nakup + zviera
print(nakupyazvierata)
print(3*zviera)
print("Dunčo" in zviera)

# narozdiel od string sú listy v Pythone mutable (meniteľné), tzv. že môžem prepísať hodnotu prvku
prazdny[0] = 1000
print(prazdny)

hodnoty = [15, 30, 80, 50, 100, 1]
print(len(hodnoty))
print(sum(hodnoty))
print(min(hodnoty))
print(max(hodnoty))