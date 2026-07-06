'''
Create an empty stack and push the values 5, 10, 15, 20 into it. Display
the stack.
'''

class Stack:
    def __init__(self):
        self.stack = []

s = Stack()

s.stack.append(5)
s.stack.append(10)
s.stack.append(15)
s.stack.append(20)

print("Stack:", s.stack)