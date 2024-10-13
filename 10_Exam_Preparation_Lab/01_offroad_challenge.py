from collections import deque

initial_fuel = [int(el) for el in input().split()]
additional_consumption_indexes = deque([int(el) for el in input().split()])
amount_of_fuel_needed = deque([int(el) for el in input().split()])

reached_altitudes = 0
max_altitudes_reached = len(initial_fuel)

while initial_fuel and additional_consumption_indexes and amount_of_fuel_needed:
    current_fuel_quantity = initial_fuel.pop()
    current_additional_consumption_index = additional_consumption_indexes.popleft()
    fuel_needed = amount_of_fuel_needed.popleft()

    result = current_fuel_quantity - current_additional_consumption_index

    if result >= fuel_needed:
        reached_altitudes += 1
        print(f"John has reached: Altitude {reached_altitudes}")
        continue
    else:
        print(f"John did not reach: Altitude {reached_altitudes + 1}")
        break

if max_altitudes_reached > reached_altitudes and reached_altitudes:
    print("John failed to reach the top.")
    print(f"Reached altitudes: ", end="")
    print(', '.join(f"Altitude {x}" for x in range(1, reached_altitudes + 1)))
elif max_altitudes_reached > reached_altitudes and not reached_altitudes:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
if max_altitudes_reached == reached_altitudes:
    print("John has reached all the altitudes and managed to reach the top!")
