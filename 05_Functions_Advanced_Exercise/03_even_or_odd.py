def even_odd(*args):
    command = args[-1]
    return [num for num in args[:-1] if num % 2 == 0] if command == "even" \
        else [num for num in args[:-1] if num % 2 != 0]

    # if command == "even":
    #     return [num for num in args[:-1] if num % 2 == 0]
    # else:
    #     return [num for num in args[:-1] if num % 2 != 0]


even_odd(1, 2, 3, 4, 5, "even")
