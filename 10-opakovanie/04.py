import tkinter as tk
import random

def akciaTlacidla():
    global pocetPokusov
    pocetPokusov += 1
    cisloMOJE=int(Textbox.get())
    if cisloMOJE < cisloPC:
        label.config(text=f"Dal si menšie číslo\nPokusy: {pocetPokusov}")
    elif cisloMOJE > cisloPC:
        label.config(text=f"Dal si väčšie číslo\nPokusy: {pocetPokusov}")
    else:
        label.config(text=f"Uhádol si! Počet pokusov: {pocetPokusov}")
        

root = tk.Tk()
root.geometry("200x200")

cisloPC=random.randint(0, 9)
pocetPokusov = 0

label=tk.Label(root, text=cisloPC)
label.pack()

Textbox=tk.Entry(root)
Textbox.pack()

button=tk.Button(root, text="Hadaj", command=akciaTlacidla)
button.pack()

root.mainloop()