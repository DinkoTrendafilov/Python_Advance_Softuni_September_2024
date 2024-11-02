n, m = map(int, input().split())

first_set = {int(input()) for _ in range(n)}
second_set = {int(input()) for _ in range(m)}

repeated_numbers = first_set.intersection(second_set)

print(*repeated_numbers, sep="\n")
