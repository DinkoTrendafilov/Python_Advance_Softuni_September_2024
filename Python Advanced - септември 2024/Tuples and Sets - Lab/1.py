my_numbers = tuple(int(x) for x in input().split())

geometric_average = None
my_numbers = list(my_numbers)
my_numbers.sort()
my_numbers = tuple(my_numbers)

if len(my_numbers) % 2 == 1:
    geometric_average = my_numbers[len(my_numbers) // 2]
else:
    geometric_average = (my_numbers[len(my_numbers) // 2 - 1] * my_numbers[len(my_numbers) // 2]) ** (1 / 2)

print(f"Length of tuple is: {len(my_numbers)}")
print(f"Sum of tuple is: {sum(my_numbers)}")
print(f"Algebra Average of tuple is: {sum(my_numbers) / len(my_numbers)}")
print(f"Geometric Average of tuple is: {geometric_average}")
print(*my_numbers)
print(f"Max number of tuple is: {max(my_numbers)}")
print(f"Min number of tuple is: {min(my_numbers)}")

