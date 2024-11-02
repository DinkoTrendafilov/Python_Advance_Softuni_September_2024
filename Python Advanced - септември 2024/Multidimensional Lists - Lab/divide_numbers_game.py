range_numbers = int(input("Enter range of number: "))

counter = []
dictionary = {}
prime_numbers = []
complex_numbers = []

for number in range(1, range_numbers + 1):
    for num in range(1, number + 1):
        if number % num == 0:
            counter.append(num)
            if number not in dictionary:
                dictionary[number] = []
            dictionary[number].append(num)

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-len(kv[1]), kv[0])))

for (number, times) in sorted_dictionary.items():
    if number not in (1, 2) and len(times) > 2:
        complex_numbers.append(number)
    elif number not in (1, 2) and len(times) <= 2:
        prime_numbers.append(number)
    # print(f"Number: {number:_} is divide to:  {' '.join(str(x) for x in times)}  | {len(times):_} times.")
    print(f"Number: {number:_} | {len(times):_} times.")

print(f"{'-' * 113}")
# print(f"Complex numbers count: {len(complex_numbers):_} --- {' '.join(str(x) for x in complex_numbers)}")
# print(f"Simple numbers count: {len(simple_numbers):_} --- {' '.join(str(x) for x in simple_numbers)}")
print(f"Complex numbers count: {len(complex_numbers):_} --> {(len(complex_numbers) / (range_numbers - 2) * 100):.2f} %")
print(f"Prime numbers count: {len(prime_numbers):_} --> {(len(prime_numbers) / (range_numbers - 2) * 100):.2f} %")
print(f"Numbers in range: {len(sorted_dictionary.keys()):_} ||"
      f" {sum(len(x) for x in sorted_dictionary.values()):_} times.")
print(f"{'-' * 113}")
