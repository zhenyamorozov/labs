import turtle

bob = turtle.Turtle()

# print(bob)

bob.speed(5)

# bob.fd(100)
# bob.rt(90)
# bob.fd(100)


for i in range(0,500):
    bob.fd(20)
    bob.rt(7+i*0.1)


turtle.mainloop()