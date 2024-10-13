rows, columns = [int(el) for el in input().split(", ")]

matrix = []

for i in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = float('-inf')
sub_matrix = []
for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index + 1]
        element_under = matrix[row_index + 1][column_index]
        element_diagonal = matrix[row_index + 1][column_index + 1]

        total_sum = current_element + next_element + element_under + element_diagonal

        if max_sum < total_sum:
            max_sum = total_sum
            sub_matrix = [[current_element, next_element], [element_under, element_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
