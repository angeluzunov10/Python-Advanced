directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

size = int(input())

matrix = []
position = []
initial_armour = 300
total_enemies = 0

for row in range(size):
    matrix.append(list(input()))
    if "J" in matrix[row]:
        position = [row, matrix[row].index("J")]
        matrix[position[0]][position[1]] = "-"

    total_enemies += matrix[row].count("E")

while True:
    command = input()

    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    position = [r, c]

    if matrix[r][c] == "-":
        continue

    elif matrix[r][c] == "E":
        total_enemies -= 1
        matrix[r][c] = "-"
        if total_enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        initial_armour -= 100
        if initial_armour <= 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
            break

    elif matrix[r][c] == "R":
        initial_armour = 300
        matrix[r][c] = "-"

    matrix[r][c] = "-"

matrix[r][c] = "J"
[print(*row, sep="") for row in matrix]