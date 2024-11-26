import tkinter, random

dlzka = int(input("Zadaj dlžku štvorca:"))
pocet = int(input("Zadaj počet štvorcov"))

canva = tkinter.Canvas(width=500, height=400)
canva.pack()

for i in range(pocet):
    x = random.randint(3, 500-dlzka-3)
    y = random.randint(3, 400-dlzka-3)
    canva.create_rectangle(x, y, x+dlzka, y+dlzka, fill=random.choice(["red", "green", "blue", "yellow"]))

tkinter.mainloop()