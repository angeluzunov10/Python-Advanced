from collections import deque

quantity = int(input())
name = input()
people = deque()
while name != "Start":
    people.append(name)
    name = input()

command = input().split()

while command[0] != "End":
    if "refill" in command:
        action, liters_to_add = command
        quantity += int(liters_to_add)
    else:
        liters_to_add = int(command[0])
        if quantity >= liters_to_add:
            quantity -= liters_to_add
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    command = input().split()

print(f"{quantity} liters left")
