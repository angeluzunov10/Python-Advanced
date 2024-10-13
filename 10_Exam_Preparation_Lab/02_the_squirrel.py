directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

collected_hazelnuts = 0
goal = 3
trapped = False
out_of_bounds = False

size = int(input())

matrix = []

commands = input().split(", ")
position = []

for row in range(size):
    matrix.append(list(input()))

    if "s" in matrix[row]:
        position = [row, matrix[row].index("s")]
        matrix[position[0]][position[1]] = "*"

for command in commands:
    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        out_of_bounds = True
        print("The squirrel is out of the field.")
        break

    position = [r, c]

    if matrix[r][c] == "h":
        collected_hazelnuts += 1
        matrix[r][c] = "*"
        if collected_hazelnuts == goal:
            goal = 0
            print("Good job! You have collected all hazelnuts!")
            break
    elif matrix[r][c] == "*":
        continue
    elif matrix[r][c] == "t":
        trapped = True
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    matrix[r][c] = "*"

if goal and not trapped and not out_of_bounds:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")
