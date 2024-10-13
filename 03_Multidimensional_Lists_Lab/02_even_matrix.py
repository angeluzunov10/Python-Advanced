row_count = int(input())

matrix = []

for i in range(row_count):
    data = [int(i) for i in input().split(", ") if int(i) % 2 == 0]
    matrix.append(data)

print(matrix)