directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

rows, cols = [int(x) for x in input().split()]

matrix = []
starting_position = []
position = []

for row in range(rows):
    matrix.append(list(input()))
    if "B" in matrix[row]:
        starting_position = [row, matrix[row].index("B")]
        position = [row, matrix[row].index("B")]

while True:
    command = input()

    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < cols):
        matrix[starting_position[0]][starting_position[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    position = [r, c]

    if matrix[r][c] == "P":
        matrix[r][c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    elif matrix[r][c] == "*":
        position = [r - directions[command][0], c - directions[command][1]]
        continue
    elif matrix[r][c] == "A":
        matrix[r][c] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    matrix[r][c] = "."


[print(*row, sep="") for row in matrix]
