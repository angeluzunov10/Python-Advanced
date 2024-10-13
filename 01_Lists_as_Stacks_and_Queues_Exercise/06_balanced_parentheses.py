from collections import deque

parenthesis = deque(input())
open_parenthesis = deque()

while parenthesis:
    current_parenthesis = parenthesis.popleft()

    if current_parenthesis in "([{":
        open_parenthesis.append(current_parenthesis)
    elif not open_parenthesis:
        print("NO")
        break
    else:
        if f"{open_parenthesis.pop() + current_parenthesis}" not in "{}()[]":
            print("NO")
            break

else:
    print("YES")

# втори вариант
#
# from collections import deque
#
# expression = deque(input())
# opening_brackets = "([{"
# closing_brackets = ")]}"
#
# counter = 0
#
# while expression and counter < len(expression) / 2:
#     if expression[0] not in opening_brackets:
#         break
#     index = opening_brackets.index(expression[0])
#     if expression[1] == closing_brackets[index]:
#         expression.popleft()
#         expression.popleft()
#         expression.rotate(counter)
#         counter = 0
#     else:
#         expression.rotate(-1)
#         counter += 1
#
# if expression:
#     print("NO")
# else:
#     print("YES")
