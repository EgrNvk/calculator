from asyncio import Event


class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        result = self.number1 + self.number2
        print(f"{self.number1} + {self.number2} = {result}")
        return

    def subtraction(self):
        result = self.number1 - self.number2
        print(f"{self.number1} - {self.number2} = {result}")
        return

    def multiplication(self):
        result = self.number1 * self.number2
        print(f"{self.number1} * {self.number2} = {result}")
        return

    def division(self):
        result = self.number1 / self.number2
        print(f"{self.number1} / {self.number2} = {result}")
        return

number1=float(input("Введіть перше число - "))
number2=float(input("Введіть друге число - "))

action=input("Введіть потрібну дію (+, -, *, /) ")
if action == "+":
    Calculator(number1,number2).addition()
elif action == "-":
    Calculator(number1,number2).subtraction()
elif action == "*":
    Calculator(number1,number2).multiplication()
elif action == "/":
    Calculator(number1,number2).division()
