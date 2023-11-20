t = ('a', 'b', 'c', 'd', 'e', 1, False, (10,11,12), [21, 22,23])

print(t)
print(t[4])
print(t[:4])

# t[4] = "E"
t[-1][0] = 121

print(t)

# t[-1] = [31, 32, 33]
t[-1][0], t[-1][1], t[-1][2] = 31, 32, 33

print(t)

print(1, 2, 3)
print((1, 2, 3))

def myprint(*args):
    print(type(args))
    for i in args:
        print(i, end=" ")
    print()

myprint(1, 2, 3)
myprint((1, 2, 3))


a = 1

print(2++++++++++++3)

