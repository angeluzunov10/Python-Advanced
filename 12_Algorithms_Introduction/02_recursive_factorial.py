def recursive_factorial(num):
    if num == 1:
        return num

    return num * recursive_factorial(num - 1)


number = int(input())
print(recursive_factorial(number))
