from collections import deque
from math import floor

expression = deque(input().split())
index = 0

while index < len(expression):
    element = expression[index]
    if element == "*":
        for _ in range(index - 1):  # everything but the symbol
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == "/":
        for _ in range(index - 1):  # everything but the symbol
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif element == "-":
        for _ in range(index - 1):  # everything but the symbol
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == "+":
        for _ in range(index - 1):  # everything but the symbol
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    if element in "*/-+":
        del expression[1]   # махаме съответния знак, който вече е на индекс 1 от пренаредения списък expression
        index = 1

    index += 1

print(floor(int(expression[0])))

# второ решение
#
# from functools import reduce
# from math import floor
#
# expression = input().split()
# index = 0
#
# functions = {
#     "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
#     "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
#     "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
#     "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
# }
#
# while index < len(expression):
#     element = expression[index]
#
#     if element in "*/-+":
#         expression[0] = functions[element](index)
#         [expression.pop(1) for _ in range(index)] # pop everything including the symbol
#         index = 1
#
#     index += 1
#
# print(floor(int(expression[0])))
