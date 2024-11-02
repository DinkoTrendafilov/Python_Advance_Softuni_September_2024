numbers = tuple(float(el) for el in input().split())

numbers_dictionary = {}

for num in numbers:
    if num not in numbers_dictionary:
        numbers_dictionary[num] = numbers.count(num)

for (number, times) in numbers_dictionary.items():
    print(f"{number} - {times} times")
