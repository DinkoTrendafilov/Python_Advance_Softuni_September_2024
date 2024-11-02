import random

n = int(input("Enter number of iterations: "))
d = {}

for i in range(n):
    numbers = [1] * 16 + [0] * 36
    random.shuffle(numbers)
    hand_1 = numbers[:13]

    result = (hand_1.count(0), hand_1.count(1))

    if result in d:
        d[result] += 1
    else:
        d[result] = 1

sorted_d = dict(sorted(d.items(), key=lambda kvp: (-kvp[1], kvp[0])))

print(f"{'-' * 113}")
count = 0

for key, value in sorted_d.items():
    count += 1

    print(f"#{count}  |  Zero Points cards: {key[0]}  | "
          f" Points cards: {key[1]}  |  {value:_} times - {(value / n * 100):.2f} %")
print(f"{'-' * 113}")
