# Challange 2
class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 / self.num1

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

calculator = calculator(num1, num2)

addition_result = calculator.add()
subtraction_result = calculator.subtract()
multiplication_result = calculator.multiply()
division_result = calculator.divide()
print("addition of num1 and num2 is:",addition_result)
print("subtraction of num1 and num2 is:",subtraction_result)
print("multiplication of num1 and num2 is:",multiplication_result)
print("division of num1 and num2 is:",division_result)