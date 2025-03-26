import tkinter

canva = tkinter.Canvas(width=300, height=300)
canva.pack()

def enko(x, y):
    canva.create_rectangle(x, y, x+10, y+10, fill="black")
enko(10,10)
enko(30,10)
enko(50,10)
x = 10
y = 10
pocet = 5
for i in range(pocet):
    x += 60



tkinter.mainloop() 