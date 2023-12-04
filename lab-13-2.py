x=-1
y = 1 if x>0 else 0
print(y)

# powers = []
# for i in range(10):
#     powers.append(2**i)

powers = [2**i for i in range(10)]
print(powers)

powers_gen = (2**i for i in range(10))

print(powers_gen)
print(next(powers_gen))
print(next(powers_gen))
print(next(powers_gen))

for j in powers_gen:
    print(j)

def powersof2():
    n = 0
    while True:
        yield 2**n
        n += 1
print()
# for k in powersof2():
#     print(k)



print( all(letter == 't' for letter in 'stake') )

myset = {"banana", "apple", "orange"}
print(myset)
print(type(myset))
myset.add("pineapple")
myset.add("banana")
print(myset)
print(type(sorted(myset)))
anotherset = {1, 2, 3, False, "banana"}
print(anotherset)
anotherset.add(True)
anotherset.add(0)
print(anotherset)
print(1==True)

print(myset & anotherset)
print(myset - anotherset)

from collections import Counter
cou = Counter("just a string")
pass

# def mydefault():
#     return 123

from collections import defaultdict
mydict = defaultdict(lambda : 123)
mydict['k1'] = "value1"

print(mydict['k1'])
print(mydict['k5'])

myfunc = lambda n: 2**n
print(myfunc(10))


from collections import namedtuple
Snake = namedtuple("Snake", ["name", "length"])
snake1 = Snake("alice", 10)
snake2 = Snake("Bob", 20)
print(snake1)
print(snake2)
pass


def onemorefunc(required_par="bus", *args, **kwargs):
    print(required_par)
    print(args)
    print(kwargs)
    pass

onemorefunc(555, par1=100, par2=200)
