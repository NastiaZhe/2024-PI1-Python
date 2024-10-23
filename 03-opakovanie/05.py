roky = 15
mesiace = 8
dni = 23
dnizarok = 365
dnizamesiac = 30
celkovedni = (roky * dnizarok) + (mesiace * dnizamesiac) + dni
hodiny = celkovedni * 24
sekundy = hodiny * 3600
print(f"počet dní je {celkovedni}")
print(f"počet hodín je {hodiny}")
print(f"počet sekúnd je {sekundy}")