#from tkinter import *
#rom tkinter import ttk
#root = Tk()
#frm = ttk.Frame(root, padding=10)
#frm.grid()
#ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#root.mainloop()
    



import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

def akcia():
    label.config(text=Textbox.get())
    
label=tk.Label(root, text="Som LABEL")
label.pack()

Textbox=tk.Entry(root)
Textbox.pack()

button=tk.Button(root, text="Som TLACIDLO", command=akcia)
button.pack

root.mainloop()
