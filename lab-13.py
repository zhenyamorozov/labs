# generator expression
gen = (x**2 for x in range(10))

print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# generator function
def gen_odds():
    n = 1
    while True:
        yield n
        n += 2

print(next(gen_odds()))

# for i in gen_odds():
#     print(i)


# any() and all()
print( any( letter == 't' for letter in 'stake' ) )


# sets
theset = {"banana", "apple", "pomegranate"}
print(theset)
theset.add("pineapple")
theset.add("apple")
print(theset)
second_set = {1, 2, 3, False, True}
print(second_set)


# counters
from collections import Counter
cou = Counter("any sequence")
print(cou)
print(Counter("customers")==Counter("storescum"))


# defaultdict
from collections import defaultdict
my_dict = defaultdict(lambda : "no value")
my_dict['k1'] = "v1"
print(my_dict['k1'])
print(my_dict['k3'])

# lambda functions - inline function definition
def triple(x):
    return x*3
print(triple(4))

triple = lambda x: x*3
print(triple(4))


# named tuples - for simple classes with no methods
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
print(Point)
p = Point(100, 200)
print(p)


# args, kwargs
def print_all(*args, **kwargs):
    print(args, kwargs)

print_all("one", 2, 3, andalso="something", andmore=42)
