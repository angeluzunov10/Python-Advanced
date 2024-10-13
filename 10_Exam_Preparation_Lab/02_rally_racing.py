def find_tunnel_exit(route):
    for row in range(size):
        if "T" in route[row]:
            return row, route[row].index("T")


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

size = int(input())

racing_number = int(input())

race_route = [input().split() for _ in range(size)]

distance_covered = 0
row, col = 0, 0
symbol = None

while True:
    command = input()

    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    next_row = direction_mapper[command][0]
    next_col = direction_mapper[command][1]

    row += next_row
    col += next_col

    symbol = race_route[row][col]

    if symbol == ".":
        distance_covered += 10
    elif symbol == "T":
        distance_covered += 30
        race_route[row][col] = "."
        row, col = find_tunnel_exit(race_route)

        race_route[row][col] = "."
    elif symbol == "F":
        distance_covered += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

race_route[row][col] = "C"

print(f"Distance covered {distance_covered} km.")
[print(''.join(row))for row in race_route]
