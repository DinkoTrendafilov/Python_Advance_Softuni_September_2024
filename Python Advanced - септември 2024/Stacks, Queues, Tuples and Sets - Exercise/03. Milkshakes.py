from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
milks = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and milks and milkshakes != 5:
    curr_choco = chocolates.pop()
    curr_milk = milks.popleft()

    if curr_milk <= 0 and curr_choco <= 0:
        continue
    elif curr_choco <= 0:
        milks.appendleft(curr_milk)
        continue
    elif curr_milk <= 0:
        chocolates.append(curr_choco)
        continue

    if curr_milk == curr_choco:
        milkshakes += 1

    else:
        milks.append(curr_milk)
        chocolates.append(curr_choco - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milks) or 'empty'}")
