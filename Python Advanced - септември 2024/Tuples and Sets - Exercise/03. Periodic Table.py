n = int(input())

my_set = set()

for _ in range(n):
    for el in input().split():
        my_set.add(el)

print(*my_set, sep="\n")
