fruits = input().split()

result = [fruit for fruit in fruits if len(fruit) % 2 == 0]

print(*result, sep="\n")
