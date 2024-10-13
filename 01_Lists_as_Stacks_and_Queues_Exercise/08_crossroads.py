from collections import deque

passed_cars_count = 0

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()

command = input()
crash = False
while command != "END":
    if command != "green":
        cars.append(command)
    else:
        current_green_window = green_light_duration

        while current_green_window > 0 and cars:
            car = cars.popleft()

            time = current_green_window + free_window_duration

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                crash = True
            current_green_window -= len(car)
            passed_cars_count += 1

    if crash:
        break
    command = input()
if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars_count} total cars passed the crossroads.")
