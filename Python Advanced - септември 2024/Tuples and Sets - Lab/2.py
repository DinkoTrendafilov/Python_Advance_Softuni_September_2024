number_one = float(input("Enter first number: "))
number_two = float(input("Enter second number: "))

average_1 = (number_one + number_two) / 2
average_2 = (number_one * number_two) ** (1 / 2)

print(f"{'-' * 113}")
print(f"Number one is: {number_one}")
print(f"Number two is: {number_two}")
print(f"{number_one} * {number_two}  =  {(number_one * number_two):_}")
print("Algebra Average of the two numbers:", average_1)
print("Geometric Average of the two numbers:", average_2)
diff = (average_1 / average_2) * 100 - 100
print(f"Percentage difference between Algebra and Geometric Average: {diff:.2f} %")
print(f"{'-' * 113}")
