def is_in_boundaries(row_index, col_index, n):
    return 0 <= row_index < n and 0 <= col_index < n


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

n = int(input())

board = []

amount = 100
player_position = None

for row_index in range(n):
    data = list(input())
    if "G" in data:
        player_position = [row_index, data.index("G")]
    board.append(data)

direction = input()

while direction != "end":
    current_row_index, current_col_index = player_position
    row_movement, col_movement = direction_mapper[direction]
    next_row_index = current_row_index + row_movement
    next_col_index = current_col_index + col_movement

    if not is_in_boundaries(next_row_index, next_col_index, n):
        print("Game over! You lost everything!")
        exit()

    symbol = board[next_row_index][next_col_index]
    board[next_row_index][next_col_index] = "G"
    board[current_row_index][current_col_index] = "-"
    player_position = [next_row_index, next_col_index]

    if symbol == "W":
        amount += 100

    elif symbol == "P":
        amount -= 200
        if amount <= 0:
            amount = 0
            print("Game over! You lost everything!")
            exit()

    elif symbol == "J":
        amount += 100000
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {amount}$")
        [print(*row, sep="") for row in board]
        exit()

    direction = input()

print(f"End of the game. Total amount: {amount}$")
[print(*row, sep="") for row in board]