n = int(input())
unique_users = set()
for _ in range(n):
    unique_users.add(input())

print(*unique_users, sep="\n")


# задачата в 1 ред
# print(*({input() for _ in range(int(input))}), sep="\n")
