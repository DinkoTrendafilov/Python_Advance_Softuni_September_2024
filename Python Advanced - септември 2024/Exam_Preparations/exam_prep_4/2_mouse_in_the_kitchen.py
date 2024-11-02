row, col = [int(x) for x in input().split(",")]

matrix = []
mouse_position = ()
total_cheese_count = 0

for r in range(row):
    current_row = list(input())
    matrix.append(current_row)
    if "M" in current_row:
        mouse_position = (r, current_row.index("M"))
    if "C" in current_row:
        total_cheese_count += current_row.count("C")

direction_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break
    current_row, current_col = mouse_position

    new_row = mouse_position[0] + direction_mapper[command][0]
    new_col = mouse_position[1] + direction_mapper[command][1]

    if not (0 <= new_row < row and 0 <= new_col < col):
        print("No more cheese for tonight!")
        break

    element = matrix[new_row][new_col]

    if element == "C":
        matrix[new_row][new_col] = "M"
        matrix[current_row][current_col] = "*"
        mouse_position = (new_row, new_col)
        total_cheese_count -= 1
        if total_cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif element == "T":
        matrix[new_row][new_col] = "M"
        matrix[current_row][current_col] = "*"
        mouse_position = (new_row, new_col)
        print("Mouse is trapped!")
        break

    elif element == "@":
        continue
    else:
        matrix[new_row][new_col] = "M"
        matrix[current_row][current_col] = "*"
        mouse_position = (new_row, new_col)


for row in matrix:
    print("".join(row))
