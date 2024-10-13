rows, columns = [int(i) for i in input().split(", ")]
matrix = []
sum_of_elements = 0
for row in range(rows):
    elements = [int(i) for i in input().split(", ")]
    matrix.append(elements)
    sum_of_elements += sum(elements)
print(sum_of_elements)
print(matrix)
