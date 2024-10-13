from collections import deque

circle = deque(input().split())
n_toss = int(input())
counter = 1

while len(circle) != 1:
    if counter % n_toss == 0:
        print(f"Removed {circle.popleft()}")
    else:
        circle.append(circle.popleft())
    counter += 1

print(f"Last is {circle.popleft()}")

# това е друго решение с метода .rotate()
#
# from collections import deque
#
# circle = deque(input().split())
# n_toss = int(input()) - 1
#
# while len(circle) > 1:
#     circle.rotate(-n_toss)
#     removed_kid = circle.popleft()
#     print(f"Removed {removed_kid}")
#
# print(f"Last is {circle.popleft()}")
