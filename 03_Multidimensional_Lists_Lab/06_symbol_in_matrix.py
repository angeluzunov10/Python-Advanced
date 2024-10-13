dimensions = int(input())
matrix = []

for i in range(dimensions):
    matrix.append(list(input()))

searched_symbol = input()

for i in range(dimensions):
    for j in range(len(matrix[i])):
        if matrix[i][j] == searched_symbol:
            print(f"({i}, {j})")
            exit()

print(f"{searched_symbol} does not occur in the matrix")
