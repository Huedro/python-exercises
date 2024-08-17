# Write a Python program to create a calculator class.
# Include methods for basic arithmetic operations.


class Calculator:
    def __init__(self, num_1, num_2, operator):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operator = operator

        if self.operator == "+":
            self.Addition()
        if self.operator == "-":
            self.Subtraction()
        if self.operator == "*":
            self.Multiplication()
        if self.operator == "/":
            self.Division()

    def Addition(self):
        print(self.num_1 + self.num_2)

    def Subtraction(self):
        print(self.num_1 - self.num_2)

    def Multiplication(self):
        print(self.num_1 * self.num_2)

    def Division(self):
        print(self.num_1 / self.num_2)


txt = input("Enter an operation (Ex: 1 + 1):")
x_array = txt.split()

calculator = Calculator(int(x_array[0]), int(x_array[2]), x_array[1])
