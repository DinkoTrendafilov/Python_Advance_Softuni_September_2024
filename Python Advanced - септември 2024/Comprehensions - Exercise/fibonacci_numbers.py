n = int(input("Enter needed count of numbers: "))

first_number = 0
second_number = 1

numbers = [first_number]
print()
for _ in range(1, n):
    print(f"First number: {first_number:_} | Second number: {second_number:_}")
    numbers.append(second_number)
    first_number, second_number = second_number, first_number + second_number

print()
print(*[f"{number:_}" for number in numbers])
print(f"Sum of Fibonacci numbers in sequence is: {(sum(numbers)):_}")
