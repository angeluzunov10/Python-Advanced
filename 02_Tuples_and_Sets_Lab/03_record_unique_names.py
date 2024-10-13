number_of_names = int(input())
set_of_names = set()

for _ in range(number_of_names):
    name = input()
    set_of_names.add(name)

for name in set_of_names:
    print(name)
