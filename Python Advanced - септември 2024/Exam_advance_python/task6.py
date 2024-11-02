import random

n = int(input("Enter number of iterations: "))
number_of_rounds = int(input("Enter number of rounds: "))

dictionary = {}
total_result = []
average_points = number_of_rounds * (((500 * 3) + (300 * 1)) / 1_000)

for _ in range(n):
    wins = 0
    draws = 0
    losses = 0
    points = 0

    for _ in range(number_of_rounds):
        random_number = random.randint(1, 1_000)  # 500-300-200  |  wins - draws - losses
        if random_number in range(1, 501):
            wins += 1
            points += 3
        elif random_number in range(501, 801):
            draws += 1
            points += 1
        else:
            losses += 1

    results = (wins, draws, losses, points)
    total_result.append(results)

for el in total_result:
    if el not in dictionary:
        dictionary[el] = 1
    else:
        dictionary[el] += 1

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[0][3], -kv[0][0], -kv[0][1], -kv[0][2])))
print(f"{'-' * 113}")
print("Statistic: ")
print(f"{'-' * 113}")

counter = 0
most_popular_key = None
for (key, value) in sorted_dictionary.items():
    if value == max(sorted_dictionary.values()):
        most_popular_key = key
    counter += 1
    print(
        f"#{counter:_} - Points: {key[3]} | Wins: {key[0]} - Draws: {key[1]} - Losses: {key[2]} |"
        f" Times: {value:_} - {(value / n * 100):.2f} %")

print(f"{'-' * 113}")
print(f"Average points: {average_points:.2f} - {(average_points / number_of_rounds):.2f}")
print(f"Max points: {max([key[3] for key in sorted_dictionary])} - "
      f"{(max([key[3] for key in sorted_dictionary]) / number_of_rounds):.2f}")
print(f"Min points: {min([key[3] for key in sorted_dictionary])} - "
      f"{(min([key[3] for key in sorted_dictionary]) / number_of_rounds):.2f}")
print(f"Total max points is: {number_of_rounds * 3}")
print(f"Most popular result: Points: {most_popular_key[3]} | Wins {most_popular_key[0]} - "
      f"Draws: {most_popular_key[1]} - Losses: {most_popular_key[2]} | "
      f"{(max(sorted_dictionary.values())):_} times - {((max(sorted_dictionary.values())) / n * 100):.2f} %")
print(f"{'-' * 113}")

d = {}
for el in total_result:
    if el[3] in d:
        d[el[3]] += 1
    else:
        d[el[3]] = 1
print()
print(f"{'-' * 113}")
sorted_d = dict(sorted(d.items(), key=lambda kv: (-kv[1], kv[0])))
counter_1 = 0
for points, times in sorted_d.items():
    counter_1 += 1
    print(f"#{counter_1} | Points: {points} - Times: {times:_} - {(times / n * 100):.2f} %")
print(f"{'-' * 113}")
