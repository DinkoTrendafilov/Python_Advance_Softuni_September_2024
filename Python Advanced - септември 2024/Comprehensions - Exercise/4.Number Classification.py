numbers = [int(x) for x in input().split(", ")]

even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]
positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]

print(f"Positive: {', '.join(str(x) for x in positive_numbers)}")
print(f"Negative: {', '.join(str(x) for x in negative_numbers)}")
print(f"Even: {', '.join(str(x) for x in even_numbers)}")
print(f"Odd: {', '.join(str(x) for x in odd_numbers)}")
