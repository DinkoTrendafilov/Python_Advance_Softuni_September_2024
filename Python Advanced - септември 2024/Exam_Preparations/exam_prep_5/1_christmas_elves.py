from collections import deque

elves = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

total_toys = 0
total_energy = 0
iterations = 0

while elves and materials:
    elf = elves.popleft()
    material = materials[-1]

    if elf < 5:
        continue

    iterations += 1
    current_toys_count = 0

    if iterations % 3 == 0:
        material *= 2
        current_toys_count += 1

    if elf >= material:
        total_energy += material
        elf -= material

        if iterations % 5 != 0:
            current_toys_count += 1
            elf += 1
        else:
            current_toys_count = 0

        materials.pop()
    else:
        elf *= 2
        current_toys_count = 0

    total_toys += current_toys_count
    elves.append(elf)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")
if elves:
    print(f"Elves left: {', '.join(map(str, elves))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
