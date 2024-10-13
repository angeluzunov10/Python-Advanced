from collections import deque

worms = deque([int(i) for i in input().split()])    # from last
holes = deque([int(i) for i in input().split()])    # from first

matches = 0
fit_hole_worms = 0
while worms and holes:
    last_worm_value = worms.pop()
    first_hole_value = holes.popleft()
    if last_worm_value == first_hole_value:
        matches += 1
        continue
    else:
        worms.append(last_worm_value - 3)
        last_worm_value = worms.pop()
        fit_hole_worms += 1
        if last_worm_value <= 0:
            continue
        else:
            worms.append(last_worm_value)

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if not fit_hole_worms:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(i) for i in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(i) for i in holes])}")

# Решение от Инес
# from collections import deque
#
# worms = [int(i) for i in input().split()]
# holes = deque([int(i) for i in input().split()])
#
# matches = 0
# all_worms_count = len(worms)
#
# while worms and holes:
#     current_worm = worms[-1]
#     current_hole = holes[0]
#
#     if current_worm == current_hole:
#         worms.pop()
#         holes.popleft()
#         matches += 1
#     else:
#         holes.popleft()
#         worms[-1] -= 3
#
#         if worms[-1] <= 0:
#             worms.pop()
#
# if matches:
#     print(f"Matches: {matches}")
# else:
#     print(f"There are no matches.")
#
# if not worms and matches == all_worms_count:
#     print("Every worm found a suitable hole!")
# elif not worms and matches < all_worms_count:
#     print("Worms left: none")
# else:
#     print(f"Worms left: {', '.join([str(el) for el in worms])}")
#
# if not holes:
#     print("Holes left: none")
# else:
#     print(f"Holes left: {', '.join([str(el) for el in holes])}")
