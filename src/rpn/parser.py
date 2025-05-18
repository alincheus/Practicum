class RPNParser:
    def evaluate(self, expression):
        stack = []
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }

        for token in expression.split():
            if token in operators:
                if len(stack) < 2:
                    return None  
                y, x = stack.pop(), stack.pop()
                stack.append(operators[token](x, y))
            else:
                stack.append(float(token))
        
        return stack[0] if stack else None  
