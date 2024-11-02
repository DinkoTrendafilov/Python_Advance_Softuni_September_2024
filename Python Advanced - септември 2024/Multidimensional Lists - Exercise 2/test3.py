def fibonacci_numbers(n):
    a, b = 0, 1

    while b < n:
        print(b, end=" ")
        a, b = b, a + b


m = int(input())
fibonacci_numbers(m)

print()
