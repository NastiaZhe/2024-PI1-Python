import tkinter

canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(20, 10, 30, 20, fill="black")
canvas.create_rectangle(30, 10, 40, 20, fill="black")
canvas.create_rectangle(40, 10, 50, 20, fill="black")

canvas.create_rectangle(10, 20, 20, 30, fill="black")
canvas.create_rectangle(10, 30, 20, 40, fill="black")
canvas.create_rectangle(10, 40, 20, 50, fill="black")
canvas.create_rectangle(10, 50, 20, 60, fill="black")
canvas.create_rectangle(10, 60, 20, 70, fill="black")
canvas.create_rectangle(10, 70, 20, 80, fill="black")

canvas.create_rectangle(50, 20, 60, 30, fill="black")
canvas.create_rectangle(50, 30, 60, 40, fill="black")
canvas.create_rectangle(50, 40, 60, 50, fill="black")
canvas.create_rectangle(50, 50, 60, 60, fill="black")
canvas.create_rectangle(50, 60, 60, 70, fill="black")
canvas.create_rectangle(50, 70, 60, 80, fill="black")

canvas.create_rectangle(20, 40, 30, 50, fill="black")
canvas.create_rectangle(30, 40, 40, 50, fill="black")
canvas.create_rectangle(40, 40, 50, 50, fill="black")

canvas.create_rectangle(70, 20, 80, 30, fill="black")
canvas.create_rectangle(80, 20, 90, 30, fill="black")
canvas.create_rectangle(90, 20, 100, 30, fill="black")
canvas.create_rectangle(100, 20, 110, 30, fill="black")
canvas.create_rectangle(110, 20, 120, 30, fill="black")


tkinter.mainloop()