from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes_prepared = 0

while milkshakes_prepared != 5 and chocolates and milk_cups:
    last_chocolate = chocolates.pop()
    first_cup = milk_cups.popleft()

    if last_chocolate <= 0 and first_cup <= 0:
        continue
    elif last_chocolate <= 0:
        milk_cups.appendleft(first_cup)
        continue
    elif first_cup <= 0:
        chocolates.append(last_chocolate)
        continue

    if first_cup != last_chocolate:
        milk_cups.append(first_cup)
        chocolates.append(last_chocolate - 5)
    else:
        milkshakes_prepared += 1

print("Great! You made all the chocolate milkshakes needed!" if milkshakes_prepared == 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join(f'{x}' for x in chocolates)}" if chocolates else "Chocolate: empty")
print(f"Milk: {', '.join(f'{x}' for x in milk_cups)}" if milk_cups else "Milk: empty")
