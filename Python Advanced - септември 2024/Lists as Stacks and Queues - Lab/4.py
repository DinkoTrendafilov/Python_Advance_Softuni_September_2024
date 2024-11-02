import random

n = int(input("Enter number of iterations: "))

total_points = []
dictionary = {}

for _ in range(n):
    points = 0
    cards = [card for card in range(1, 53)]
    random_result = random.sample(cards, 13)

    for el in random_result:
        if el in (1, 14, 27, 40):
            points += 4
        elif el in (11, 24, 37, 50):
            points += 1
        elif el in (12, 25, 38, 51):
            points += 2
        elif el in (13, 26, 39, 52):
            points += 3

    total_points.append(points)

for el in total_points:
    if el in dictionary:
        dictionary[el] += 1
    else:
        dictionary[el] = 1

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))
avg_points = sum(total_points) / n

print(f"{'-' * 113}")
for (points, times) in sorted_dictionary.items():
    print(f"Points: {points:02d} | Times: {times:_} | {(times / n * 100):.2f} %")
print(f"{'-' * 113}")
print(f"Min points: {min(sorted_dictionary.keys())} | Max points: {max(sorted_dictionary.keys())}")
print(f"{'-' * 113}")
print(f"Average points in set is: {avg_points:.2f}")
print(f"Needed average points: {10.00}")
print(f"Sum of total points: {(sum(total_points)):_}")

if avg_points >= 10.00:
    print("Congratulations, you have good set!")
else:
    print("Sorry, you have bad set!.")
print(f"{'-' * 113}")
