import random

n = int(input("Enter number of iterations: "))
result = []
dictionary = {}

for _ in range(n):
    numbers = [num for num in range(1, 11)]
    random.shuffle(numbers)
    counter = 0
    elements = [1, 2, 3]

    while True:
        counter += 1
        current_element = numbers[0]

        if current_element in range(1, 4):
            elements.remove(current_element)

        numbers.pop(0)
        if not elements:
            result.append(counter)
            break

for el in result:
    if el not in dictionary:
        dictionary[el] = 1
    else:
        dictionary[el] += 1

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for (number, count) in sorted_dictionary.items():
    print(f"Attempts {number:02d} to remove [1,2,3]  |  {count:_} times   |    {(count / n * 100):.2f} %")
