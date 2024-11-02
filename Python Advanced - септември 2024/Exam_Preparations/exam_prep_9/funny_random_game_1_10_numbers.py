import random

n = int(input("Enter number of iterations: "))
result = []
dictionary = {}
left_win = 0
left_super_win = 0
right_win = 0
right_super_win = 0
total_left_points = 0
total_right_points = 0

for _ in range(n):
    numbers = [num for num in range(1, 11)]
    random.shuffle(numbers)
    left_part = numbers[:5:]
    right_part = [num for num in numbers if num not in left_part]
    result.append([sum(left_part), sum(right_part)])

    if sum(left_part) > sum(right_part):
        left_win += 1
    else:
        right_win += 1

    if sum(left_part) == 40:
        left_super_win += 1
    elif sum(right_part) == 40:
        right_super_win += 1

for el in result:
    total_left_points += el[0]
    total_right_points += el[1]
    if tuple(el) not in dictionary:
        dictionary[tuple(el)] = 1
    else:
        dictionary[tuple(el)] += 1

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kvp: (-kvp[1], -kvp[0][0], kvp[0][1])))

print(f"{'-' * 113}")
counter = 0
for (combination, count) in sorted_dictionary.items():
    counter += 1
    print(f"#{counter} - The combination {combination} appears {count:_} times - {(count / n * 100):.2f} %")
print(f"{'-' * 113}")

print(f"Left part wins: {left_win:_} - {(left_win / n * 100):.2f} %")
print(f"SUPER Left part wins: {left_super_win:_} - {(left_super_win / n * 100):.2f} %")
print(f"Right part wins: {right_win:_} - {(right_win / n * 100):.2f} %")
print(f"SUPER Right part wins: {right_super_win:_} - {(right_super_win / n * 100):.2f} %")
print()
print(f"Total points scored by left part: {total_left_points:_} | {total_left_points / n}")
print(f"Total points scored by right part: {total_right_points:_} | {total_right_points / n}")
print(f"Total combinations: {len(sorted_dictionary)}")
print(f"{'-' * 113}")
