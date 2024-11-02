from collections import deque

food_quantity = int(input())
orders = deque(int(el) for el in input().split())

print(max(orders))

for order in orders.copy():
    if food_quantity >= order:
        food_quantity -= order
        orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(el) for el in orders)}")
