import random

n = int(input("Enter number of total iterations: "))
m = int(input("Enter number of inner cycle: "))

d = {}

for _ in range(n // m):
    result = []
    for i in range(m):
        number = random.randint(1, 2)
        result.append(number)

    res = (result.count(1), result.count(2))
    if res not in d:
        d[res] = 1
    else:
        d[res] += 1

sorted_d = dict(sorted(d.items(), key=lambda kvp: (-kvp[1], kvp[0])))

print(f"{'-' * 113}")
counter = 0

for key, value in sorted_d.items():
    counter += 1
    print(f"#{counter} | Result {key}: {value:_} times - {(value / (n / 20) * 100):.2f} %")
print(f"{'-' * 113}")
print(f"Total sum of 1 is: {(sum([key[0] for key in sorted_d])):_} "
      f"- MAX VALUE is: {max(key[0] for key in sorted_d)} - MIN VALUE is: {min(key[0] for key in sorted_d)}")
print(f"Total sum of 2 is: {(sum([key[1] for key in sorted_d])):_} "
      f"- MAX VALUE is: {max(key[1] for key in sorted_d)} - MIN VALUE is: {min(key[1] for key in sorted_d)}")
print(f"Iterations count is: {(sum(sorted_d.values())):_}")
print(f"{'-' * 113}")
