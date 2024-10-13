def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def power(num1, num2):
    return num1 ** num2


sign_mapper = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "^": power
}


def execute_expression(exp):
    num1_text, sign, num2_text = exp.split()
    num1 = float(num1_text)
    num2 = int(num2_text)

    return sign_mapper[sign](num1, num2)
