data = input()

elements = []
rows = []
cols = []

for el in data:
    if el.isdigit():
        elements.append(int(el))

rows = elements[::2]
cols = elements[1::2]

print(*elements)
print(*rows)
print(*cols)
