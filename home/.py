def sirka(meno_suboru):
    with open(meno_suboru, encoding='utf-8') as f:
        return max(len(riadok) for riadok in f)
# 2. Функція zlomky(meno_suboru)
# python
# Копіювати
# Редагувати
def zlomky(meno_suboru):
    from fractions import Fraction
    with open(meno_suboru, encoding='utf-8') as f:
        hodnoty = [Fraction(riadok.strip()) for riadok in f if riadok.strip()]
    pocet = len(hodnoty)
    sucet = float(sum(hodnoty))
    priemer = sucet / pocet if pocet > 0 else 0
    print(f'počet = {pocet}')
    print(f'súčet = {sucet:.2f}')
    print(f'priemer = {priemer:.2f}')
# 3. Функція vypis_do_ramiku(meno_suboru)
# python
# Копіювати
# Редагувати
def vypis_do_ramiku(meno_suboru):
    with open(meno_suboru, encoding='utf-8') as f:
        riadky = [riadok.rstrip('\n') for riadok in f]
    sirka = max(len(riadok) for riadok in riadky)
    print('*' * (sirka + 4))
    for riadok in riadky:
        print(f'* {riadok.ljust(sirka)} *')
    print('*' * (sirka + 4))
# 4. Функція vykresli_text(meno_suboru, velkost=16)
# python
# Копіювати
# Редагувати
def vykresli_text(meno_suboru, velkost=16):
    import tkinter
    global canvas
    canvas.delete("all")
    with open(meno_suboru, encoding='utf-8') as f:
        y = 10
        for riadok in f:
            canvas.create_text(10, y, anchor='nw', text=riadok.rstrip('\n'),
                               font=('consolas', velkost))
            y += velkost + 2
# 5. Функція kresli(meno_suboru)
# python
# Копіювати
# Редагувати
def kresli(meno_suboru):
    import tkinter
    global canvas
    canvas.delete("all")
    with open(meno_suboru) as f:
        skupina = []
        for riadok in f:
            riadok = riadok.strip()
            if not riadok:
                if len(skupina) > 1:
                    canvas.create_line(skupina)
                    for x, y in skupina:
                        canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')
                skupina = []
            else:
                x, y = map(int, riadok.split())
                skupina.append((x, y))
        if len(skupina) > 1:
            canvas.create_line(skupina)
            for x, y in skupina:
                canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')
# 6. Функція vykresli_stvorce(meno_suboru, n=6)
# python
# Копіювати
# Редагувати
def vykresli_stvorce(meno_suboru, n=6):
    import tkinter
    global canvas
    canvas.delete("all")
    x = 10
    with open(meno_suboru, encoding='utf-8') as f:
        farby = f.readlines()
    pocet = len(farby)
    for i in range(n):
        farba = farby[i % pocet].strip()
        canvas.create_rectangle(x, 10, x + 25, 35, fill=farba)
        x += 30
# 7. Функція vyrob(meno_suboru, pocet, text)
# python
# Копіювати
# Редагувати
def vyrob(meno_suboru, pocet, text):
    with open(meno_suboru, 'w', encoding='utf-8') as f:
        f.write("i = 0\n")
        f.write(f"while i < {pocet}:\n")
        f.write(f"    print('{text}')\n")
        f.write("    i += 1\n")
# 8. Функція body_na_kruznici(meno_suboru, n, r, x, y)
# python
# Копіювати
# Редагувати
from math import cos, sin, pi

def body_na_kruznici(meno_suboru, n, r, x, y):
    with open(meno_suboru, 'w') as f:
        for i in range(n + 1):
            uhol = 2 * pi * i / n
            xi = round(x + r * cos(uhol))
            yi = round(y + r * sin(uhol))
            f.write(f'{xi} {yi}\n')
# 9. Функція vyhod_riadok(meno_suboru, index)
# python
# Копіювати
# Редагувати
def vyhod_riadok(meno_suboru, index):
    with open(meno_suboru, encoding='utf-8') as f:
        riadky = f.readlines()
    if index == -1:
        index = len(riadky) - 1
    if 0 <= index < len(riadky):
        del riadky[index]
        with open(meno_suboru, 'w', encoding='utf-8') as f:
            f.writelines(riadky)
# 10. Функція hladaj(skratka) для fakulty.csv
# python
# Копіювати
# Редагувати
def hladaj(skratka):
    with open('fakulty.csv', encoding='utf-8') as f:
        fakulty = [riadok.strip().split(';') for riadok in f][1:]
    pary = [(nazov, skr) for nazov, skr in [(r[0], r[1]) for r in fakulty]]
    for nazov, skr in pary:
        if skr.lower() == skratka.lower():
            return (nazov, skr)
    return '*** takuto fakultu nepoznam ***'
# 11. Функція psc(retazec) для psc-obci-sr-a-cr.csv
# python
# Копіювати
# Редагувати
def psc(retazec):
    with open('psc-obci-sr-a-cr.csv', encoding='utf-8') as f:
        riadky = [riadok.strip().split(';') for riadok in f][1:]
    zoznam = sorted([(psc, obec) for psc, obec in [(r[0], r[1]) for r in riadky]])
    for p in zoznam:
        if p[0] == retazec:
            return p
    # найменше більше
    for p in zoznam:
        if p[0] > retazec:
            return p
    return zoznam[-1]  # якщо нічого більше
# 12. Функція urob_svg(meno_suboru)
# python
# Копіювати
# Редагувати
def urob_svg(meno_suboru):
    with open(meno_suboru, encoding='utf-8') as f:
        riadky = [riadok.strip() for riadok in f if riadok.strip()]
    body = []
    max_x = max_y = 0
    for riadok in riadky:
        casti = riadok.split()
        farba = casti[0]
        coords = list(map(int, casti[1:]))
        max_x = max(max_x, max(coords[::2]))
        max_y = max(max_y, max(coords[1::2]))
        body.append((farba, coords))
    with open('obrazok.svg', 'w') as f:
        f.write(f'<svg height="{max_y}" width="{max_x}" xmlns="http://www.w3.org/2000/svg">\n')
        for farba, coords in body:
            bodky = " ".join(f'{coords[i]},{coords[i+1]}' for i in range(0, len(coords), 2))
            f.write(f'<polygon points="{bodky}" style="fill:{farba}" />\n')
        f.write('</svg>')