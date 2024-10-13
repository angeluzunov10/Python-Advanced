n = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]

primary_diagonal = [matrix[r][r] for r in range(n)]
secondary_diagonal = [matrix[r][n - r - 1] for r in range(n)]

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

