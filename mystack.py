class Stack:
    def __init__(self):
        self.__stack = []
    
    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        if len(self.__stack):
            val = self.__stack[-1]
            del self.__stack[-1]
            return val
        else:
            return None

    def __str__(self):
        return f"This stack contans: {self.__stack}"

    def __add__(self, other):
        sumStack = Stack()
        while True:
            val = self.pop()
            if val==None:
                break
            else:
                sumStack.push(val)
        while True:
            val = other.pop()
            if val==None:
                break
            else:
                sumStack.push(val)
        return sumStack


myStack1 = Stack()
myStack2 = Stack()

myStack1.__stack = "banana"
myStack1.push(1)
myStack1.push(2)
myStack2.push(10)
myStack2.push(20)
myStack1.push(3)
myStack1.push(5)

myStack3 = myStack1 + myStack2

myStack1.pop()
print(myStack3)

# print(myStack1.pop())
# print(myStack1.pop())
# print(myStack1.pop())
# print(myStack1.pop())
# print(myStack1.pop())

