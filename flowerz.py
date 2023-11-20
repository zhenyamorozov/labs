import turtle
import math

crawler = turtle.Turtle()


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



polyline(crawler, 8, 100, 45)

# arc(crawler, 100, 90)
crawler.penup()
crawler.fd(50)
crawler.lt(90)
crawler.fd(50+100*1.4//2)
# crawler.lt(90)
crawler.pendown()


for i in range(7):
    arc(crawler, 100, 360//7)
    crawler.lt(180-360//7)
    arc(crawler, 100, 360//7)
    crawler.lt(180)

turtle.mainloop()