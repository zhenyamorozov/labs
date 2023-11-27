from turtle import Turtle, mainloop
import math
width = 1000
height = 500
scale_x = 40
scale_y = 40

t = Turtle()
t.speed(speed=0)
t.hideturtle()

def drawOX(width=1000):
    t.penup()
    t.goto(-width/2, 0)
    t.pendown()
    t.goto(width/2, 0)
    t.penup()
    t.goto(width/2-10, 0+5)
    t.pendown()
    t.goto(width/2, 0)
    t.goto(width/2-10, 0-5)
    t.penup()
    t.goto(0, 0)

def drawOY(height=1000):
    t.penup()
    t.goto(0, -height/2)
    t.pendown()
    t.goto(0, height/2)
    t.penup()
    t.goto(0-5, height/2-10)
    t.pendown()
    t.goto(0, height/2)
    t.goto(0+5, height/2-10)
    t.penup()
    t.goto(0, 0)

def drawF(f, color="black"):
    t.color(color)
    min_x = -width/2 / scale_x
    max_x = width/2 / scale_x
    firstStep = True
    x = min_x
    while x < max_x:
        y = f(x)
        if firstStep:
            t.penup()
            firstStep = False
        else:
            t.pendown()
            
        t.goto(x*scale_x, y*scale_y)
        x += 1/scale_x
    pass

def f1(x):
    return math.cos(x)

def f2(x):
    return math.cos(10*x)

# def f1(x):
#     return math.cos(x)

# def f2(x):
#     return math.tan(x)

def f3(x):
    return f1(x)+f2(x)

drawOX(width)
drawOY(height)
drawF(f1, "blue")
drawF(f2, "green")
drawF(f3, "red")

mainloop()