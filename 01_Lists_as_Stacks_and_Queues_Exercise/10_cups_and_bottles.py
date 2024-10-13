from collections import deque

wasted_litters_of_water = 0

cups = deque([int(cup) for cup in input().split()])
bottles = deque([int(bottle) for bottle in input().split()])

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_litters_of_water += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print(f"Cups:", *cups)
else:
    print(f"Bottles:", *bottles)

print(f"Wasted litters of water: {wasted_litters_of_water}")
