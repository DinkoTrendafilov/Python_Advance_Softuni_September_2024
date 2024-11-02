import random

n = int(input("Enter number of iterations: "))
m = int(input("Enter needed % probability: "))
#
# max_number = 100
#
# for i in range(n):
#     for _ in range(max_number):
#         random_number = random.randint(1, max_number)
#         if random_number in range(1, max_number + 1):
#             max_number -= 0
#         else:
#             max_number -= 1
#     print(f"Iteration: {i + 1} --- Number: {max_number}")
#
# print(f"Sum is: {max_number}")
# print()
# print(f"Result is: {(0.9 ** n) * 100}")
# print(f"Length is: {len(str((0.9 ** n) * 100))}")
#
# for i in range(1, n + 1):
#     print(f"The probability of the number being less than or equal to {i} is {(0.9 ** i) * 100} %")


d = {}

for _ in range(n):
    res = []
    for _ in range(100):
        random_number = random.randint(1, 100)
        if random_number in range(1, m + 1):
            res.append(1)
        else:
            res.append(0)
    if sum(res) not in d:
        d[sum(res)] = 1
    else:
        d[sum(res)] += 1

sorted_dictionary = dict(sorted(d.items(), key=lambda kv: (-kv[1], kv[0])))

max_key_value = max(sorted_dictionary.keys())
min_key_value = min(sorted_dictionary.keys())

print(f"Probability {m} %")
for (key, value) in sorted_dictionary.items():
    print(f"Number: {key:_}   ||  {value:_} times   ||  {((value / n) * 100):.2f} %")

up_sum = sum([v for k, v in sorted_dictionary.items() if k >= m + 1 and k <= max_key_value])
under_sum = sum({v for k, v in sorted_dictionary.items() if k in range(min_key_value, m)})
equall_sum = sum({v for k, v in sorted_dictionary.items() if k == m})

print()
print(f"Up Sum is: {up_sum:_} || {(up_sum / n * 100):.2f} %")
print(f"Equall Sum is: {equall_sum:_} || {(equall_sum / n * 100):.2f} %")
print(f"Under Sum is: {under_sum:_} || {(under_sum / n * 100):.2f} %")
print()
print(f"Max number is: {max_key_value}")
print(f"Min number is: {min_key_value}")
