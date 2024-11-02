n = int(input())

dictionary = {}

for _ in range(n):
    split_command = input().split()
    name = split_command[0]
    grade = float(split_command[1])

    if name not in dictionary:
        dictionary[name] = []

    dictionary[name].append(grade)

for (name, grades) in dictionary.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join(f'{el:.2f}' for el in grades)}"
    print(f"{name} -> {formatted_grades} {f'(avg: {average_grade:.2f})'}")
