rows, columns = [int(i) for i in input().split()]

matrix = [[el for el in input().split()] for i in range(rows)]

total_squares_in_matrix = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        current_element = matrix[i][j]
        next_element = matrix[i][j + 1]
        under_element = matrix[i + 1][j]
        diagonal_element = matrix[i + 1][j + 1]
        if current_element == next_element and current_element == under_element and current_element == diagonal_element:
            total_squares_in_matrix += 1

print(total_squares_in_matrix)