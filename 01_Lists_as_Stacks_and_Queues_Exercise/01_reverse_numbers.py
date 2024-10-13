# from collections import deque
#
# numbers = deque(input().split())
#
# for i in range(len(numbers)):
#     print(numbers.pop(), end=" ")

# второ решение
# numbers = deque(input().split())
# numbers.reverse()
# print(" ".join(numbers))

numbers = input().split()
for i in range(len(numbers)):
    print(numbers.pop(), end=" ")