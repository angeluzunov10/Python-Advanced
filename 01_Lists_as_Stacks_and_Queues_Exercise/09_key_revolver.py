from collections import deque


price_for_each_bullet = int(input())
gun_barrel_size = int(input())
bullets = deque(int(bullet) for bullet in input().split())
locks = deque(int(lock) for lock in input().split())
intelligence_value = int(input())

bullets_in_barrel = gun_barrel_size
bullets_shot = 0
while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)
    bullets_in_barrel -= 1
    bullets_shot += 1

    if bullets_in_barrel == 0 and bullets:
        if len(bullets) >= gun_barrel_size:
            bullets_in_barrel = gun_barrel_size
        else:
            bullets_in_barrel = len(bullets)

        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence_value - (price_for_each_bullet * bullets_shot)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")

