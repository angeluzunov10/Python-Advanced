from collections import deque
from datetime import datetime, timedelta
robots = {}

for r in input().split(";"):
    name, time_needed = r.split("-")        # "ROB-15" -> name = ROB, time_needed = 15
    robots[name] = [int(time_needed), 0]         # 0-та е за да отброяваме колко време му остава, за да е свободен

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1    # {"ROB": [15, 15]}
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue
    robot_name, data = free_robots[0]  # robots_name = "ROB", data = [15, 0]
    robots[robot_name][1] = data[0]    # {"ROB": [15, 15]}

    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
