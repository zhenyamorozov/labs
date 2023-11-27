class Stack:
    """ This class implements a simple stack. It assumes vlaues are integers """

    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val


class SumStack(Stack):
    """ This subclass implements a stack which also tracks its own sum value """
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def push(self, val):
        Stack.push(self, val)
        self.__sum += val

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def __str__(self):
        return f"The contents of this SumStack is {self._Stack__stack}, the sum is {self.__sum}"    # use manual name mangling to access superclass' private attribute




mystack = SumStack()

mystack.push(1)
mystack.push(2)
mystack.push(3)

print(mystack)

print(mystack.pop())
print(mystack)
print(mystack.pop())
print(mystack)

pass


class CountStack(Stack):
    """ This subclass implements a stack which also tracks the amount of items in it """
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0
        
    def push(self, val):
        self.__count += 1
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__count -= 1
        return val

    def __str__(self):
        return f"The contents of this CountStack is {self._Stack__stack}, the amount of items is {self.__count}"    # use manual name mangling to access superclass' private attribute



myCountstack = CountStack()

myCountstack.push(10)
myCountstack.push(20)
myCountstack.push(30)

print()
print(myCountstack)

print(myCountstack.pop())
print(myCountstack)
print(myCountstack.pop())
print(myCountstack)

pass
