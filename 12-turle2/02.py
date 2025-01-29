import turtle

dlzka = 10

t = turtle.Turtle()
# t.speed(0)

def stvorec(d):
    for i in range(4):
        t.forward(d)
        t.left(90)

def okno(d):
    for i in range(3):
        stvorec(d)
        t.forward(dlzka * 2)
        t.left(90)
        t.forward(dlzka)
        t.left(90)
        t.forward(dlzka)
        t.left(90)
        



def domcek (d):
    for i in range(4):
        t.fillcolor('red')
        t.begin_fill()
        okno(dlzka)
        t.right(90)
        t.penup()
        t.left(90)
        t.forward(dlzka * 3)
        t.pendown()
        t.left(90)
        t.forward(dlzka * 2)
        t.left(90)
        t.forward(dlzka * 4)
        t.left(90)
        t.forward(dlzka * 4)
        t.left(90)
        t.forward(dlzka * 4)
        t.left(90)
        t.forward(dlzka * 2)
        t.end_fill()
        t.fillcolor('black')
        t.begin_fill()
        t.forward(-dlzka * 2)
        t.right(45)
        t.forward(dlzka * 3)
        t.left(90)
        t.forward(dlzka * 3)
        t.end_fill()
        t.penup()
        t.left(45)
        t.forward(dlzka * 2)
        t.left(90)
        t.forward(dlzka * 6)
        t.pendown()
        


def ulica (d):
    for i in range(4):
        domcek(dlzka)
        t.penup()
        t.right(90)       
        t.forward(dlzka * 9)
        t.right(90)
        t.forward(dlzka * 20)
        t.right(90)
        t.forward(dlzka * 2)
        t.right(90)        
        t.forward(dlzka)
        t.pendown()
        

ulica (dlzka)

turtle.mainloop()








