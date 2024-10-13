def negatives_vs_positives(*args):
    positives_sum = sum(num for num in args if num > 0)
    negatives_sum = sum(num for num in args if num < 0)

    print(f"{negatives_sum}")
    print(f"{positives_sum}")

    if abs(negatives_sum) > positives_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


negatives_vs_positives(*[int(i) for i in input().split()])
