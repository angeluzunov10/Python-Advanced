longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [element.split(",") for element in input().split("-")]

    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

formatted_intersection = ", ".join(str(x) for x in longest_intersection)
print(f"Longest intersection is [{formatted_intersection}] with length {len(longest_intersection)}")

# моето по-подробно решение
#
# n = int(input())
# longest_intersection = set()
#
# for _ in range(n):
#     first, second = input().split("-")
#
#     first_start, first_end = [int(a) for a in first.split(",")]
#     second_start, second_end = [int(b) for b in second.split(",")]
#
#     first_set = set()
#     second_set = set()
#
#     for number in range(first_start, first_end + 1):
#         first_set.add(number)
#     for number in range(second_start, second_end + 1):
#         second_set.add(number)
#     current_intersection = set(first_set & second_set)
#
#     if len(current_intersection) > len(longest_intersection):
#         longest_intersection = current_intersection
#
# formatted_intersection = f"{', '.join([f'{i}' for i in longest_intersection])}"
#
# print(f"Longest intersection is [{formatted_intersection}] with length {len(longest_intersection)}")
