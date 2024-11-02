n = int(input())

matrix = []
ship_position = ()
catch = 0

# Четене на матрицата и намиране на позицията на кораба
for row in range(n):
    current_row = list(input())
    matrix.append(current_row)
    if "S" in current_row:
        ship_position = (row, current_row.index("S"))

directions_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    direction = input()

    if direction not in directions_mapper:
        break

    next_row = (ship_position[0] + directions_mapper[direction][0]) % n
    next_col = (ship_position[1] + directions_mapper[direction][1]) % n

    matrix[ship_position[0]][ship_position[1]] = "-"
    ship_position = (next_row, next_col)

    element = matrix[next_row][next_col]

    if element == "W":
        matrix[next_row][next_col] = "-"
        catch = 0
        # Коригиран печат на последната позиция на кораба при водовъртеж
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{next_row}, {next_col}]")
        break

    elif element.isdigit():
        catch += int(element)
        matrix[next_row][next_col] = "-"

    # Успех при достигане на квотата
    if catch >= 20:
        matrix[next_row][next_col] = "S"
        print("Success! You managed to reach the quota!")
        break

    matrix[next_row][next_col] = "S"

# Неуспех при недостигане на квотата
if catch < 20:
    print("You didn't catch enough fish and didn't reach the quota!")
    print(f"You need {20 - catch} tons of fish more.")
    print(f"Last coordinates of the ship: [{ship_position[0]}, {ship_position[1]}]")

# Отпечатване на количеството уловена риба
if catch:
    print(f"Amount of fish caught: {catch} tons.")

# Отпечатване на финалната матрица
for row in matrix:
    print("".join(row))