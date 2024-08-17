# Write a Python program to create a class representing a stack data structure.
# Include methods for pushing and popping elements.


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print("Cannot pop from an empty stack.")

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


stack1 = Stack()

stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)

stack1.pop()
stack1.pop()

print(stack1)
print("Stack1 size:", stack1.size())
