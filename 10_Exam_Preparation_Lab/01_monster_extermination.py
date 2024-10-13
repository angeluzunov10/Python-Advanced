from collections import deque

monsters_armour = deque([int(x) for x in input().split(",")])
striking_impact = [int(x) for x in input().split(",")]
monsters_killed = 0

while monsters_armour and striking_impact:
    current_monster = monsters_armour.popleft()
    current_soldier = striking_impact.pop()

    if current_soldier >= current_monster:
        monsters_killed += 1
        current_soldier -= current_monster
        if striking_impact:
            striking_impact[-1] += current_soldier
        elif not striking_impact and current_soldier > 0:
            striking_impact.append(current_soldier)
    else:
        current_monster -= current_soldier
        monsters_armour.append(current_monster)

if not monsters_armour:
    print("All monsters have been killed!")

if not striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")