square_matrix_size = int(input())
matrix = []
diagonal_sum = 0
for i in range(square_matrix_size):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
