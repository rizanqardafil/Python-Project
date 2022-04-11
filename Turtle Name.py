import turtle
import random
from alphabet import alphabet

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed("slowest")
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(2)

def displaymessage(message,fontsize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontsize, y + dot[1]*fontsize)
        myPen.pendown()
        
      x += fontsize
      
    if character == " ":
      x += fontsize
    x += characterSpacing 

fontsize = 30
characterSpacing = 1
fontColor = "#FF00FF"

message = "Fahrizal Arda!"
displaymessage(message,fontsize,fontColor,-190,0)
turtle.mainloop()