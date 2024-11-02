n = int(input())

matrix = []
jet_fighter_position = ()
initial_armor = 300
total_enemies = 0


for row in range(n):
    current_row = list(input())
    matrix.append(current_row)
    if "J" in current_row:
        jet_fighter_position = (row, current_row.index("J"))
    total_enemies += current_row.count("E")


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


while True:
    direction = input()

    new_row = jet_fighter_position[0] + direction_mapper[direction][0]
    new_col = jet_fighter_position[1] + direction_mapper[direction][1]


    if not (0 <= new_row < n and 0 <= new_col < n):
        continue


    matrix[jet_fighter_position[0]][jet_fighter_position[1]] = "-"
    jet_fighter_position = (new_row, new_col)


    if matrix[new_row][new_col] == "R":
        initial_armor = 300
        matrix[new_row][new_col] = "J"


    elif matrix[new_row][new_col] == "-":
        matrix[new_row][new_col] = "J"
        continue


    elif matrix[new_row][new_col] == "E":
        total_enemies -= 1
        initial_armor -= 100
        matrix[new_row][new_col] = "J"

        if total_enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break


    if initial_armor <= 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")
        break


for row in matrix:
    print("".join(row))