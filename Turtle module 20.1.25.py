'''import turtle
star=turtle.Turtle()
star.right(0)
star.forward(100)
for i in range(4):
    star.right(90)
    star.forward(100)
turtle.done()

import turtle
screen = turtle.Screen()
screen.bgcolor("pink")
spiral = turtle.Turtle()
spiral.speed(20)
spiral.width(3)
colors = ["red","green","orange", "yellow",  "blue", "purple","teal"]
for i in range(360):
    spiral.color(colors[i % 7]) 
    spiral.forward(i)
    spiral.right(50)
    spiral.left(100)
turtle.done()

import turtle
screen = turtle.Screen()
screen.bgcolor("pink")
spiral = turtle.Turtle()
spiral.speed(20)
spiral.width(3)
spiral.left(56)
colors = ["red"]
for i in range(10):
    spiral.color(colors[i % 1]) 
    spiral.forward(i)
    spiral.left(0)
    spiral.forward(10)
spiral.circle(50,100)
spiral.circle(25,100)
spiral.forward(10)
for i in range(10):
    spiral.color(colors[i % 1]) 
    spiral.forward(i)
    spiral.left(0)
    spiral.forward(1)

spiral.circle(25,100)
spiral.circle(1,1)

turtle.done()'''
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
spiral = turtle.Turtle()
spiral.speed(20)
spiral.width(3)
colors = ["red","green","orange", "yellow",  "blue", "purple","teal"]
for i in range(360):
    spiral.color(colors[i % 7]) 
    spiral.forward(i)
    spiral.right(0)
    spiral.left(100)
turtle.done()
