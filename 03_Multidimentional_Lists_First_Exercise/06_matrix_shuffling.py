rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if len(command) != 5:
        print("Invalid input!")
        continue

    action, first_element_row, first_element_col, second_element_row, second_element_col = command
    first_element_row = int(first_element_row)
    first_element_col = int(first_element_col)
    second_element_row = int(second_element_row)
    second_element_col = int(second_element_col)
    if action != "swap" \
            or not 0 <= first_element_row < rows \
            or not 0 <= first_element_col < cols \
            or not 0 <= second_element_row < rows \
            or not 0 <= second_element_col < cols:
        print("Invalid input!")
        continue

    matrix[first_element_row][first_element_col], matrix[second_element_row][second_element_col] = \
        matrix[second_element_row][second_element_col], matrix[first_element_row][first_element_col]
    [print(*row) for row in matrix]

