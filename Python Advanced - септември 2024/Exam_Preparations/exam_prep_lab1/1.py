n = int(input("Enter count of numbers: "))

fibonacci_numbers = []
old = 0
new = 1

while len(fibonacci_numbers) < n:
    fibonacci_numbers.append(old)
    old, new = new, old + new

for i in range(len(fibonacci_numbers)):
    num = f"{fibonacci_numbers[i]:_}"
    if i == len(fibonacci_numbers) - 1:
        print(fibonacci_numbers[i])
    else:
        print(fibonacci_numbers[i], end=", ")
print()
for i in range(len(fibonacci_numbers)):
    print(f"Index: {i} - Number is: {fibonacci_numbers[i]}")
print()
print(f"Sum is: {(sum(fibonacci_numbers)):_}")

print()
for i in range(1, len(fibonacci_numbers)):
    result = fibonacci_numbers[i] / fibonacci_numbers[i - 1] if fibonacci_numbers[i - 1] != 0 else 0
    print(f"Ratio of {fibonacci_numbers[i]} to {fibonacci_numbers[i - 1]} is: {result:.6f}")
