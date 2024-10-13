def multiply(*args: int):
    result = 1
    for el in args:
        result *= el
    return result


print(multiply(1, 4, 5))
