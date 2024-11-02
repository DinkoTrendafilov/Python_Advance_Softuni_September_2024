n = int(input())

matrix = []
bee_position = ()
bee_energy = 15
nectar = 0
restored_energy = False

for row in range(n):
    current_row = list(input())
    matrix.append(current_row)
    if "B" in current_row:
        bee_position = (row, current_row.index("B"))

prow, pcol = bee_position

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    direction = input()
    matrix[prow][pcol] = "-"

    prow = (prow + direction_mapper[direction][0]) % n
    pcol = (pcol + direction_mapper[direction][1]) % n

    bee_energy -= 1

    element = matrix[prow][pcol]

    if element.isdigit():
        nectar += int(element)

    elif element == "H":
        matrix[prow][pcol] = "B"
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if bee_energy <= 0:
        if nectar >= 30 and not restored_energy:
            diff = nectar - 30
            bee_energy += diff
            nectar = 30
            restored_energy = True

            if bee_energy <= 0:
                print("This is the end! Beesy ran out of energy.")
                matrix[prow][pcol] = "B"
                break
        else:
            print("This is the end! Beesy ran out of energy.")
            matrix[prow][pcol] = "B"
            break

    matrix[prow][pcol] = "B"

for row in matrix:
    print("".join(row))
