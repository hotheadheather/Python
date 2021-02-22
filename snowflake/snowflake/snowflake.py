import turtle
import random

pat = turtle.Turtle()
turtle.Screen().bgcolor("pink")
colors = ["cyan", "purple", "white", "blue", "red", "orange", "violet"]
pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()



for i in range(10):
    for i in range(2):

        pat.forward(200)
        pat.right(60)
        pat.forward(50)
        pat.right(120)
    pat.color(random.choice(colors))


    pat.right(36)
