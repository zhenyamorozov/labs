# generator expression
gen = ( i*2 for i in range(10) )

print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# generator function
def odds():
    n = 1
    while True:
        yield n
        n += 2

# for i in odds():
#     print(i)

print([letter == 'k' for letter in 'snake'])
print( any(letter == 't' for letter in 'snake') )

myset = {"apple", "banana", "peach"}
print(myset)
print(type(myset))
myset.add("pineapple")
myset.add("banana")
print(myset)

otherset = {1, 2, 3, "banana", False}
print(otherset)
otherset.add(True)
print(otherset)

print(True==1)
print(myset & otherset)
print(myset | otherset)
print(myset - otherset)

from collections import Counter
cou = Counter("any sequence")
print(cou)
print(Counter("customers")==Counter("storescum"))


from collections import defaultdict

# def dictdefault():
#     return 0

mydict = defaultdict(lambda : 0)
mydict['k1'] = "value1"
print(mydict)
print(mydict['k1'])
print(mydict['k3'])

triple = lambda x : x*3
print(triple(5))


from collections import namedtuple

Point = namedtuple("Point", ("x", "y") )

p1 = Point(10,20)
p2 = Point(y=100, x=200)
# p2.x = 500
pass


def func(*args, **kwargs):
    print(args)
    print(kwargs)

print(func(1, 2, 3, par1=100, par2=200))
