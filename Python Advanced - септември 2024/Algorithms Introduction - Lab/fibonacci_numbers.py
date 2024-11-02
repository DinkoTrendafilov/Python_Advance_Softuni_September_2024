count = int(input("Enter your count of Fibonacci sequence: "))

fibonacci_numbers = []
old = 0
new = 1

while len(fibonacci_numbers) < count:
    fibonacci_numbers.append(old)
    old, new = new, old + new

for i in range(len(fibonacci_numbers)):
    print(f"Index: {i:_}  ---  Value: {fibonacci_numbers[i]:_}")
print()
print(*[f"{num:_}" for num in fibonacci_numbers])
print(f"Sum of first {count} numbers of fibonacci sequence is: {(sum(fibonacci_numbers)):_}")
