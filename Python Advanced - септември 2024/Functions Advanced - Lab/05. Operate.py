from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x + y, args)
    elif operator == "-":
        return reduce(lambda x, y: x - y, args)
    elif operator == "/":
        if len(args) > 1:
            return reduce(lambda x, y: x / y, args)
        else:
            return "Error: Division by zero"
    elif operator == "*":
        return reduce(lambda x, y: x * y, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
