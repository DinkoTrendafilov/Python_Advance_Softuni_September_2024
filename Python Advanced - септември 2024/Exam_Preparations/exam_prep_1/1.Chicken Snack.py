from collections import deque

amount_of_money = [int(x) for x in input().split()]
food_prices = deque([int(x) for x in input().split()])

eaten_quantity_food = 0

while amount_of_money and food_prices:
    current_money = amount_of_money[-1]
    current_food_price = food_prices[0]

    if current_money == current_food_price:
        eaten_quantity_food += 1
        amount_of_money.pop()
        food_prices.popleft()

    elif current_money > current_food_price:
        eaten_quantity_food += 1
        diff = current_money - current_food_price

        if len(amount_of_money) > 1:
            amount_of_money[-2] += diff
        else:
            amount_of_money[-1] += diff
        amount_of_money.pop()
        food_prices.popleft()
    else:
        amount_of_money.pop()
        food_prices.popleft()

if eaten_quantity_food:
    if eaten_quantity_food >= 4:
        print(f"Gluttony of the day! Henry ate {eaten_quantity_food} foods.")
    elif eaten_quantity_food == 1:
        print(f"Henry ate: {eaten_quantity_food} food.")
    else:
        print(f"Henry ate: {eaten_quantity_food} foods.")

else:
    print("Henry remained hungry. He will try next weekend again.")
