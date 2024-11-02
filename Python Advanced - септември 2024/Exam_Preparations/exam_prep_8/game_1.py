import random

n = int(input("Enter number of total iterations: "))
m = int(input("Enter number of inner cycle: "))

d = {}

for _ in range(n // m):
    result = []
    for i in range(m):
        number = random.randint(1, 4)
        result.append(number)

    res = (result.count(1), result.count(2), result.count(3), result.count(4))
    if res not in d:
        d[res] = 1
    else:
        d[res] += 1

sorted_d = dict(sorted(d.items(), key=lambda kvp: (-kvp[0][0], -kvp[0][1], -kvp[0][2])))

print(f"{'-' * 113}")
counter = 0
max_1 = 0
max_2 = 0
max_3 = 0
max_4 = 0


for key, value in sorted_d.items():
    counter += 1
    max_1 = max(max_1, key[0])
    max_2 = max(max_2, key[1])
    max_3 = max(max_3, key[2])
    max_4 = max(max_4, key[3])

    print(f"#{counter:_} | Result {key}: {value:_} times - {(value / (n / m) * 100):.2f} %")
print(f"{'-' * 113}")
print(f"Total sum of 1 is: {(sum([key[0] for key in sorted_d])):_} "
      f"- MAX VALUE is: {max(key[0] for key in sorted_d)} - MIN VALUE is: {min(key[0] for key in sorted_d)}")
print(f"Total sum of 2 is: {(sum([key[1] for key in sorted_d])):_} "
      f"- MAX VALUE is: {max(key[1] for key in sorted_d)} - MIN VALUE is: {min(key[1] for key in sorted_d)}")
print(f"Total sum of 3 is: {(sum([key[2] for key in sorted_d])):_} "
      f"- MAX VALUE is: {max(key[2] for key in sorted_d)} - MIN VALUE is: {min(key[2] for key in sorted_d)}")
print(f"Total sum of 4 is: {(sum([key[3] for key in sorted_d])):_} "
      f"- MAX VALUE is: {max(key[3] for key in sorted_d)} - MIN VALUE is: {min(key[3] for key in sorted_d)}")
print()
print(f"Iterations count is: {(sum(sorted_d.values())):_}")
print(f"Max 1 is: {max_1}")
print(f"Max 2 is: {max_2}")
print(f"Max 3 is: {max_3}")
print(f"Max 4 is: {max_4}")
print(f"{'-' * 113}")
