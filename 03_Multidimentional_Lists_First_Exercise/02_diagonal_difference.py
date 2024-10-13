n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

primary_diagonal_sum, secondary_diagonal_sum = 0 , 0

for i in range(n):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][n - i - 1]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))
