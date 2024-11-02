import random

n = int(input("Enter number of iterations: "))
d = {}

for i in range(n):
    numbers = [4] * 4 + [3] * 4 + [2] * 4 + [1] * 4 + [0] * 36
    random.shuffle(numbers)
    hand_1 = numbers[::4]

    result = (sum(hand_1))

    if result in d:
        d[result] += 1
    else:
        d[result] = 1

sorted_d = dict(sorted(d.items(), key=lambda kvp: (-kvp[1], kvp[0])))

print(f"{'-' * 113}")
count = 0
total_points = 0

for key, value in sorted_d.items():
    count += 1
    total_points += key * value

    print(f"#{count} | Result {key}: {value:_} times - {(value / n * 100):.2f} %")
print(f"{'-' * 113}")
print()
print(f"Total points: {total_points:_} | Average points: {(total_points / n):.2f}")
print(f"Max points in set: {max(key for key in sorted_d)}")
print(f"Min points in set: {min(key for key in sorted_d)}")
print(f"{'-' * 113}")
