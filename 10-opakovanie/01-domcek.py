import tkinter, random

canvas_width = 600
canvas_height = 600
x = 50
y = 50
farba = "green"
dlzka = 20
 
canvas=tkinter.Canvas()
canvas.pack()

def dom(x, y, dlzka, farba):
    polovica = dlzka / 2
    stvertina = dlzka / 4

    # canvas.create_polygon(x0, y0, x1, y1, x2, y2) # vykresli mnohouholnik v tomto prípade trojuholnik, lebo prejde cez tri body (x, y)
    canvas.create_polygon(x, y + polovica, x + polovica, y, x + dlzka, y + polovica)
    canvas.create_rectangle(x, y + polovica, x + dlzka, y + polovica + dlzka, fill=farba)
    canvas.create_rectangle(x + stvertina, y + stvertina * 3, x + polovica, y + dlzka, fill= "blue")
    canvas.create_rectangle(x + stvertina, y + dlzka, x + stvertina + polovica, y + dlzka + stvertina, fill= "blue")
    canvas.create_rectangle(x + polovica, y + polovica + stvertina, x + polovica + stvertina, y + dlzka, fill= "blue")
    canvas.create_rectangle(x + polovica, y + dlzka,  x + polovica + stvertina, y + dlzka + stvertina, fill="blue")

def ulica(x, y, dlzka, pocet):
    farba1, farba2 = "red", "green"
    for i in range(pocet):
        dom(x, y, dlzka, farba1)
        x = x + dlzka + 8
        farba1, farba2 = farba2, farba1

def dedina(dlzka):
    y = 3
    for i in range(5):
        ulica(x, y, dlzka, 8)
        y = y + dlzka + 5 + dlzka / 2


dedina(30)

tkinter.mainloop()