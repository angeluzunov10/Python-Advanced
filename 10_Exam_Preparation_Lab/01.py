from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices_of_foods = deque([int(x) for x in input().split()])
change = None
products = 0

while amount_of_money and prices_of_foods:
    current_money = amount_of_money[-1]
    current_price = prices_of_foods[0]

    if current_money == current_price:
        amount_of_money.pop()
        prices_of_foods.popleft()
        products += 1

    elif current_money > current_price:
        change = current_money - current_price
        amount_of_money.pop()
        prices_of_foods.popleft()
        if len(amount_of_money) > 1:
            amount_of_money.append(amount_of_money.pop() + change)
        else:
            amount_of_money.append(change)
        products += 1

    elif current_money < current_price:
        amount_of_money.pop()
        prices_of_foods.popleft()


if products >= 4:
    print(f"Gluttony of the day! Henry ate {products} foods.")
elif products > 1:
    print(f"Henry ate: {products} foods.")
elif products == 1:
    print(f"Henry ate: {products} food.")
elif not products:
    print(f"Henry remained hungry. He will try next weekend again.")
