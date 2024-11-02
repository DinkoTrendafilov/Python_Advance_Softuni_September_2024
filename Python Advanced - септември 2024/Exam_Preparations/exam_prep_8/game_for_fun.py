import random

n = int(input("Enter number of iterations: "))

d = {}

total_result = []
best_1_row = 0
best_1_no_row = 0
best_x_row = 0
best_x_no_row = 0
best_2_row = 0
best_2_no_row = 0

res_1 = 0
res_1_no = 0
res_x = 0
res_x_no = 0
res_2 = 0
res_2_no = 0

for _ in range(n):
    numbers = ["1", "X", "2"]
    random.shuffle(numbers)
    res = numbers[0]
    total_result.append(res)
    if res not in d:
        d[res] = 1
    else:
        d[res] += 1

sorted_d = dict(sorted(d.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for el in total_result:
    if el == "1":
        res_1 += 1
        if res_1 > best_1_row:
            best_1_row = res_1
        if res_1_no > best_1_no_row:
            best_1_no_row = res_1_no

        res_1_no = 0
        res_x = 0
        res_x_no += 1
        res_2 = 0
        res_2_no += 1

    elif el == "X":
        res_x += 1
        if res_x > best_x_row:
            best_x_row = res_x
        if res_x_no > best_x_no_row:
            best_x_no_row = res_x_no

        res_x_no = 0
        res_1 = 0
        res_1_no += 1
        res_2 = 0
        res_2_no += 1

    else:
        res_2 += 1
        if res_2 > best_2_row:
            best_2_row = res_2
        if res_2_no > best_2_no_row:
            best_2_no_row = res_2_no

        res_2_no = 0
        res_x = 0
        res_x_no += 1
        res_1 = 0
        res_1_no += 1

print(f"{'-' * 113}")
print(f"Best 1 in ROW: {best_1_row}")
print(f"Best 1 in NO ROW: {best_1_no_row}")
print(f"Best X in ROW: {best_x_row}")
print(f"Best X in NO ROW: {best_x_no_row}")
print(f"Best 2 in ROW: {best_2_row}")
print(f"Best 2 in NO ROW: {best_2_no_row}")
print(f"{'-' * 113}")
for key, value in sorted_d.items():
    print(f"Result {key}: {value:_} times - {(value / n * 100):.2f} %")
print(f"{'-' * 113}")



