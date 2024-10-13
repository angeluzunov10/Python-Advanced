n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    invalid = False
    command = input()
    action, *indices = command.split()
    indices = [int(i) for i in indices]
    if action == 'END':
        break
    for row in range(n):
        if not 0 <= indices[0] <= len(matrix[row]) - 1 or not 0 <= indices[1] <= len(matrix[row]) - 1:
            print("Invalid coordinates")
            invalid = True
            break
    if invalid:
        continue
    else:
        if action == 'Add':
            matrix[indices[0]][indices[1]] += indices[2]
        elif action == 'Subtract':
            matrix[indices[0]][indices[1]] -= indices[2]

[print(*el) for el in matrix]

#  решение от упражнението
#
# size = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(size)]
#
# command = input().split()
#
# while command[0] != "END":
#     action, r, c, number = command[0], int(command[1]), int(command[2]), int(command[3])
#
#     if not (0 <= r < size and 0 <= c < size):
#         print("Invalid coordinates")
#     elif action == "Add":
#         matrix[r][c] += number
#     elif action == "Subtract":
#         matrix[r][c] -= number
#
#     command = input().split()
#
# [print(*row) for row in matrix]


