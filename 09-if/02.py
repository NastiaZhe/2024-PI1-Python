import tkinter
import random

canvas_width = int(input("Šírka plátna: "))
canvas_height = int(input("Výška plátna: "))

canvas = tkinter.Canvas(height=canvas_height, width=canvas_width)
canvas.pack()

for i in range(1000):
    a = 10
    x = random.randint(3, canvas_width-3-a)
    y = random.randint(3, canvas_height-3-a) 
    # if (x < canvas_width / 2) and (y < canvas_height / 2): # zložená podmienka, tzn. testujeme viac vlastností
    #     # medzi zložené podmienky vkladáme logické operátory (and = a zároveň, or = alebo) 
    #     farba = "blue"
    # elif (x > canvas_width / 2) and (y > canvas_height / 2):
    #     farba = "yellow"
    # elif (x > canvas_width / 2) and (y < canvas_height / 2):
    #     farba = "red"
    # elif (x < canvas_width / 2) and (y > canvas_height / 2):
    #     farba = "green"

    if x < canvas_width / 2:
        if y < canvas_height / 2:
            farba = "blue"
        else:
            farba = "green"
    else:
        if y < canvas_height / 2:
            farba = "red"
        else:
            farba = "yellow"
            
    canvas.create_oval(x, y, x + a, y + a, fill=farba, width=0)

tkinter.mainloop()