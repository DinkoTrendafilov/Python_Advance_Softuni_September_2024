n = int(input())

matrix = []
ship_position = ()
catch = 0
flag = False

for row in range(n):
    current_row = list(input())
    matrix.append(current_row)
    if "S" in current_row:
        ship_position = (row, current_row.index("S"))

directions_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    direction = input()

    if direction == "collect the nets":
        break

    next_row = (ship_position[0] + directions_mapper[direction][0]) % n
    next_col = (ship_position[1] + directions_mapper[direction][1]) % n

    matrix[ship_position[0]][ship_position[1]] = "-"
    ship_position = (next_row, next_col)

    element = matrix[next_row][next_col]

    if element == "W":
        matrix[next_row][next_col] = "-"
        catch = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{next_row},{next_col}]")
        flag = True
        break
    elif element.isdigit():
        matrix[next_row][next_col] = "-"
        catch += int(element)

    matrix[next_row][next_col] = "S"

if catch >= 20 and not flag:
    print("Success! You managed to reach the quota!")
elif catch < 20 and not flag:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - catch} tons of fish more.")

if catch and not flag:
    print(f"Amount of fish caught: {catch} tons.")

if not flag:
    for row in matrix:
        print("".join(row))
