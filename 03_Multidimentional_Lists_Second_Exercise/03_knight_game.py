n = int(input())
matrix = [list(input()) for _ in range(n)]
moves = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (1, 2),
)

removed_knights = 0
while True:
    max_attacks = 0
    best_knight = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                removes_for_current_knight = 0

                for move in moves:
                    moving_row = row + move[0]
                    moving_col = col + move[1]

                    if 0 <= moving_row < n and 0 <= moving_col < n:
                        if matrix[moving_row][moving_col] == "K":
                            removes_for_current_knight += 1

                if removes_for_current_knight > max_attacks:
                    best_knight = [row, col]
                    max_attacks = removes_for_current_knight
    if best_knight:
        r, c = best_knight
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
