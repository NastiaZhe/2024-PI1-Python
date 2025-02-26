# palindrom je reťazec, ktorý je rovnaký prí čítaní od začiatku alebo od konca
ret = input("zadaj reťazec:")

obrateny = ret[::-1]

if ret == obrateny:
    print("Reťazec", ret, "je palindrom")
else:
    print("Reťazec", ret, "nie je palindrom")