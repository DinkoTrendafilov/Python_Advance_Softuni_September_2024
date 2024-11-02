from itertools import combinations, permutations

names = [name for name in input("Enter names: ").split()]
el = int(input("Enter needed count of elements: "))

c = list(combinations(names, el))
p = list(permutations(names, el))

print("Combinations:")
print(len(c))
[print(*x, sep=" ") for x in c]
print()
print()
print(len(p))
print("Permutations:")
[print(*x, sep=" ") for x in p]

