sequence_one = set(int(x) for x in input().split())
sequence_two = set(int(x) for x in input().split())

for _ in range(int(input())):
    action, sequence, *numbers = input().split()
    command = action + " " + sequence
    if command == "Add First":
        [sequence_one.add(int(element)) for element in numbers]
    elif command == "Add Second":
        [sequence_two.add(int(element)) for element in numbers]
    elif command == "Remove First":
        [sequence_one.discard(int(element)) for element in numbers]
    elif command == "Remove Second":
        [sequence_two.discard(int(element)) for element in numbers]
    elif command == "Check Subset":
        print(sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one))

print(*sorted(sequence_one), sep=", ")
print(*sorted(sequence_two), sep=", ")

# второ решение с lambda функцията
#
# sequence_one = set(int(x) for x in input().split())
# sequence_two = set(int(x) for x in input().split())
#
# functions = {
#     "Add First": lambda x: [sequence_one.add(int(el)) for el in x],
#     "Add Second": lambda x: [sequence_two.add(int(el)) for el in x],
#     "Remove First": lambda x: [sequence_one.discard(int(el)) for el in x],
#     "Remove Second": lambda x: [sequence_two.discard(int(el)) for el in x],
#     "Check Subset": lambda x: print(sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one))
# }
#
# for _ in range(int(input())):
#     action, sequence, *numbers = input().split()
#     command = action + " " + sequence
#
#     functions[command](numbers)
#
# print(*sorted(sequence_one), sep=", ")
# print(*sorted(sequence_two), sep=", ")
