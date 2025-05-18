from src.calculations.ICalculator import ICalculator
from src.utils.math_utils import add, subtract, multiply, divide

class Calculator(ICalculator):
    
    def add(self, a, b):
        return add(a, b)

    def subtract(self, a, b):
        return subtract(a, b)

    def multiply(self, a, b):
        return multiply(a, b)

    def divide(self, a, b):
        return divide(a, b)
