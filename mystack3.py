class Stack:

    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val


class SumStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def __str__(self):
        return f"The contents is {None}, the sum is {self.__sum}"




mystack = SumStack()

mystack.push(1)
mystack.push(2)
mystack.push(3)

print(mystack)

print(mystack.pop())
print(mystack.pop())
print(mystack.pop())



pass
