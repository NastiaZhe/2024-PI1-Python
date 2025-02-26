# string v Pythone je immutable, tzn. nemeníteťný
ret = "Ahoj Svet"
# ret[0] = "a" toto nie je možné, lebo je to immutable
ret = "a" + ret[1:] # ak chceme zmeniť nejaký znak, musíme to urobiť takto
print(ret)

#reťazce vieme porovnavať

print("a" == "a")
print(ord("a")) # ord je funkcia, ktorá vráti ordinálnu (číselnú) hodnotu znak
print(ord("A")) 
print("a" > "A")
print(chr(64)) # chr() je funkcia, ktorá na základe ordinálnej hodnoty vráti znak
