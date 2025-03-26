# print(bin(255)) vypíše číslo v binárnej podobe
# print(hex(255)) vypíše číslo v hexadecimálnej podobe
# print(0b11111111) vypíše binárne číslo v desiatkovej podobe
# print(0xFF) vypíše hexadecimálne číslo v desiatkovej podobe

def dec_bin(cislo):
    binarne = "" 
    while cislo > 0:
        zvysok = cislo % 2 
        binarne = str(zvysok) + binarne
        cislo = cislo // 2
    return binarne

def dec_hex(cislo): 
    hexadecimalne = "" 
    hex = "0123456789ABCDEF"
    while cislo > 0:
        zvysok = cislo % 16 
        hexadecimalne = hex[zvysok] + hexadecimalne
        
        cislo = cislo // 16
    return hexadecimalne




cislo = 1023
print(dec_bin(cislo))
print(dec_hex(cislo))



