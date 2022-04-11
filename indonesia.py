import turtle

hr = turtle.Turtle()

hr.speed(100)


hr.setposition(-500,150)
hr.pendown()
hr.fillcolor('red')
hr.begin_fill()
hr.forward(1000)
hr.left(90)
hr.forward(300)
hr.left(90)
hr.forward(1000)
hr.left(90)
hr.forward(300)
hr.end_fill()
hr.penup

hr.setposition(0,0)
hr.pendown()
hr.fillcolor('blue')
hr.begin_fill()
hr.forward(1000)
hr.right(270)
hr.forward(300)
hr.right(270)
hr.forward(1000)
hr.right(270)
hr.forward(300)
hr.end_fill()


turtle.done()