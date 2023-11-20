from turtle import Turtle, mainloop
import math

def square(t, length=100):
    for i in range(4):
        t.fd(length)
        t.left(90)


crawler = Turtle()
# square(crawler, 50)

# crawler2 = Turtle()
# crawler2.fd(30)
# square(crawler2)



def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(crawler, 250)


mainloop()