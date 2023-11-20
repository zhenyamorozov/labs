def myprint():
    print("hey there")

def do_twice(f):
    f()
    f()


do_twice(myprint)