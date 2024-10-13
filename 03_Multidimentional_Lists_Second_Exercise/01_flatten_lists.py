matrix = [[int(x) for x in string.split()]for string in input().split("|")]
flatten_matrix = []
for index in range(len(matrix) - 1, -1, -1):
    flatten_matrix.append(matrix[index])

[[print(x, end=" ") for x in el]for el in flatten_matrix]


# второ решение, без вложени списъци
#
# line = input().split()
#
# sub_lists = []
#
# for sub_string in line[::-1]:
#     sub_lists.extend(sub_string.split())
#
# print(*sub_lists)
