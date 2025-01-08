import tkinter as tk
import random

def akciaTlacidla():
    cisloMOJE=Textbox.get()
    if cisloMOJE < cisloPC:
        label.config(text="Dal si menšie číslo")
    elif cisloMOJE > cisloPC:
        label.config(text="Dal si väčšie číslo")
    else:
        label.config(text="Uhádol si")

root = tk.Tk()
root.geometry("200x200")

cisloPC=random.randint(0, 9)
    
label=tk.Label(root, text=cisloPC)
label.pack()

Textbox=tk.Entry(root)
Textbox.pack()

button=tk.Button(root, text="Hadaj", command=akciaTlacidla)
button.pack()

root.mainloop()

