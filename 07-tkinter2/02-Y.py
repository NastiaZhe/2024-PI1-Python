import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def yko(x, y):
    canvas.create_rectangle(x, y, x+10, y+10, fill="black")
    canvas.create_rectangle(x, y+10, x+10, y+20, fill="black")
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill="black")
    canvas.create_rectangle(x+20, y+30, x+30, y+40, fill="black")
    canvas.create_rectangle(x+20, y+40, x+30, y+50, fill="black")
    canvas.create_rectangle(x+20, y+50, x+30, y+60, fill="black")
    canvas.create_rectangle(x+20, y+60, x+30, y+70, fill="black")
    canvas.create_rectangle(x+30, y+30, x+40, y+20, fill="black")
    canvas.create_rectangle(x+40, y+20, x+50, y+10, fill="black")
    canvas.create_rectangle(x+40, y+10, x+50, y, fill="black")

def riadok_y(x, y, pocet):
     for i in range(pocet):
        yko(x, y)
        x += 60

def riadky_y(x, y, pocet_riadkov, pocet_stlpcov):
    for i in range(pocet_riadkov):
        riadok_y(x, y, pocet_stlpcov)
        y += 90

yko(10, 10)
riadok_y(10, 100, 3)
riadky_y(10, 190, 3, 3)

tkinter.mainloop()
