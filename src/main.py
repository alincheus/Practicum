from src.calculations.calculator import Calculator
from src.rpn.parser import RPNParser
from src.storage.history import Storage

def main():
    calculator = Calculator()
    rpn_parser = RPNParser()
    storage = Storage()

    print("Выберите режим работы:")
    print("1. Обычные вычисления")
    print("2. Вычисления в обратной польской нотации")

    choice = input("Введите номер (1 или 2): ")

    if choice == "1":
        expr = input("Введите выражение (например, 2 + 3): ")
        a, operator, b = expr.split()
        operations = {"+": calculator.add, "-": calculator.subtract, "*": calculator.multiply, "/": calculator.divide}
        result = operations[operator](float(a), float(b))
    elif choice == "2":
        expr = input("Введите выражение в ОПН (например, 2 3 +): ")
        result = rpn_parser.evaluate(expr)
    else:
        print("Некорректный выбор!")
        return

    print(f"Результат: {result}")
    
    storage.save({"expression": expr, "result": result})
    print("Результат сохранён!")

if __name__ == "__main__":
    main()
