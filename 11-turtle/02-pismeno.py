import turtle

dlzka = 10

t = turtle.Turtle()

def stvorec(d):
    for i in range(4):
        t.forward(d)
        t.left(90)
        

def a(d):
    stvorec(dlzka)
    t.penup()
    t.forward(dlzka)
    t.pendown()

for i in range(5):
    a(dlzka) 

t.forward(-dlzka)
t.right(90)
stvorec(dlzka)

t.forward(dlzka)
t.right(90)
stvorec(dlzka)

t.penup()
t.forward(dlzka*2)
t.left(90)
t.forward(dlzka)
t.pendown()
stvorec(dlzka)

t.penup()
t.forward(dlzka)
t.right(90)
t.pendown()
stvorec(dlzka)

t.penup()
t.forward(dlzka*2)
t.left(90)
t.forward(dlzka)
t.pendown()
stvorec(dlzka)

t.penup()
t.forward(dlzka*2)
t.left(90)
t.pendown()

for i in range(5):
    a(dlzka)


turtle.mainloop