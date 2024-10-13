rows = int(input())

flattened_matrix = []

for i in range(rows):
    row_data = [int(i) for i in input().split(',')]
    flattened_matrix.extend(row_data)

print(flattened_matrix)

# второ решение само с list comprehension-и
#
# matrix = [[int(i) for i in input().split(", ")] for row in range(int(input()))]
# flattened_matrix = [element for row in matrix for element in row]
# print(flattened_matrix)
