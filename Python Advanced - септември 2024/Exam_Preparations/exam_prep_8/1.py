import random

n = int(input("Enter number of iterations: "))
f1_range = int(input("Enter range of player 1: "))
f2_range = int(input("Enter range of player 2: "))
d = {}

for _ in range(n):
    result = ""
    first_player_number = random.randint(1, f1_range)
    second_player_number = random.randint(1, f2_range)

    if first_player_number > second_player_number:
        result = "1"
    elif first_player_number == second_player_number:
        result = "X"
    else:
        result = "2"

    if result in d:
        d[result] += 1
    else:
        d[result] = 1

sorted_d = dict(sorted(d.items(), key=lambda kvp: (-kvp[1], kvp[0])))

print(f"{'-' * 113}")
for key, value in sorted_d.items():
    print(f"Result {key}: {value:_} times - {(value / n * 100):.2f} %")
print(f"{'-' * 113}")
