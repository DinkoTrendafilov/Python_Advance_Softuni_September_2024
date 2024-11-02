import random

n = int(input("Enter number of iterations: "))
d = {}

for i in range(n):
    numbers = [4] * 4 + [3] * 4 + [2] * 4 + [1] * 4 + [0] * 36
    random.shuffle(numbers)
    hand_1 = numbers[::4]

    result = (sum(hand_1), hand_1.count(0), (len(hand_1) - hand_1.count(0)))

    if result in d:
        d[result] += 1
    else:
        d[result] = 1

sorted_d = dict(sorted(d.items(), key=lambda kvp: (-kvp[0][0], -kvp[0][1], -kvp[0][2])))

print(f"{'-' * 113}")
count = 0
total_points = 0
total_0_cards = 0
total_points_cards = 0
for key, value in sorted_d.items():
    count += 1
    total_points += key[0] * value
    total_0_cards += key[1] * value
    total_points_cards += key[2] * value
    print(f"#{count} | Points: {key[0]} - Zero cards: {key[1]} - Points cards: {key[2]} | "
          f"{value:_} times - {(value / n * 100):.2f} %")
print(f"{'-' * 113}")
print()
print(f"Total points: {total_points:_} | {(total_points / n):.2f}")
print(f"Total 0 cards: {total_0_cards:_} | {(total_0_cards / n):.2f}")
print(f"Total points cards: {total_points_cards:_} | {(total_points_cards / n):.2f}")
print()
print(f"Max points in set: {max(key[0] for key in sorted_d)}")
print(f"Min points in set: {min(key[0] for key in sorted_d)}")
print(f"{'-' * 113}")
