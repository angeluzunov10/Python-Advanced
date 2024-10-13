odd_set = set()
even_set = set()
for row in range(1, int(input()) + 1):
    values_sum = sum(ord(char) for char in input()) // row

    if values_sum % 2 == 0:
        even_set.add(values_sum)
    else:
        odd_set.add(values_sum)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
