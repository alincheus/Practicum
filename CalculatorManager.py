from src.calculations.calculator import Calculator

class CalculatorManager:
    def __init__(self):
        self.calculator = Calculator()

    def calculate(self, operation, num1, num2):
        if operation == "add":
            return self.calculator.add(num1, num2)
        elif operation == "subtract":
            return self.calculator.subtract(num1, num2)
        elif operation == "multiply":
            return self.calculator.multiply(num1, num2)
        elif operation == "divide":
            return self.calculator.divide(num1, num2) if num2 != 0 else "Ошибка (деление на 0)"
