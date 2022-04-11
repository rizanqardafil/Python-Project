import turtle
from turtle import*
turtle.title("RIZAN")
screen=turtle.Screen()
screen.bgcolor("#000000")
screen.setup(620,470)
letter=turtle.Turtle()
letter.pencolor('blue')
letter.pensize(5)
letter.shape('turtle')
letter.penup()

wn = turtle.Screen()
wn.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('white')
rotate = int(180)


def Circles(t, size):
    for i in range(10):
        t.circle(size)
        size = size - 4


def ankur(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


ankur(s, 200, 10)

t1 = turtle.Turtle()
t1.speed(0)
t1.color('yellow')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10


def ankur(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


ankur(t1, 160, 10)

t2 = turtle.Turtle()
t2.speed(0)
t2.color('blue')
rotate = int(80)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5


def ankur(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


letter.goto(-250,0)
letter.pendown()
letter.right(90)#R
letter.back(120)
letter.right(90)
letter.back(70)
letter.left(90)
letter.forward(50)
letter.left(90)
letter.back(70)
letter.right(45)
letter.forward(95)
letter.penup()

letter.goto(-150, 0)#i
letter.pendown()
letter.left(135)
letter.forward(120)
letter.penup()

letter.goto(-120, 120) #z
letter.pendown()
letter.right(90)
letter.forward(90)
letter.right(125)
letter.forward(145)
letter.right(55)
letter.back(90)
letter.penup()

letter.goto(0,0) #A
letter.pendown()
letter.right(115)
letter.forward(130)
letter.left(50)
letter.back(130)
letter.forward(50)
letter.left(65)
letter.forward(65)
letter.penup()


letter.goto(120,0) #n
letter.pendown()
letter.right(90)
letter.forward(120)
letter.right(155)
letter.forward(130)
letter.right(25)
letter.back(120)

turtle.done()