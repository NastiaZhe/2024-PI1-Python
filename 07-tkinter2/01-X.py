import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def xko(x, y): # definicia funkcie, xko názov (to davame my), () sú takzvané parametre funkcie
    canvas.create_rectangle(x, y, x+10, y+10, fill="black")
    canvas.create_rectangle(x, y+10, x+10, y+20, fill="black")
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill="black")
    canvas.create_rectangle(x+20, y+30, x+30, y+40, fill="black")
    canvas.create_rectangle(x+10, y+40, x+20, y+50, fill="black")
    canvas.create_rectangle(x, y+50, x+10, y+60, fill="black")
    canvas.create_rectangle(x, y+60, x+10, y+70, fill="black")
    canvas.create_rectangle(x+30, y+30, x+40, y+20, fill="black")
    canvas.create_rectangle(x+40, y+20, x+50, y+10, fill="black")
    canvas.create_rectangle(x+40, y+10, x+50, y, fill="black")
    canvas.create_rectangle(x+30, y+40, x+40, y+50, fill="black")
    canvas.create_rectangle(x+40, y+50, x+50, y+60, fill="black")
    canvas.create_rectangle(x+40, y+60, x+50, y+70, fill="black")

def riadok_x(x, y, pocet):
     for i in range(pocet):
        xko(x, y)
        x += 60

def riadky_x(x, y, pocet_riadkov, pocet_stlpcov):
    for i in range(pocet_riadkov):
        riadok_x(x, y, pocet_stlpcov)
        y += 90

            

# xko(10, 10) # volanie funkcie, na tomto mieste sa vykoná
# xko(70, 10)
# xko(130, 10)

# x = 10
# y = 10
# pocet = 5
# for i in range(pocet):
#     xko(x, y)
#     # x = x + 60
#     x += 60

xko(10, 10)
riadok_x(10, 100, 3)
riadky_x(10, 190, 3, 3)

tkinter.mainloop()