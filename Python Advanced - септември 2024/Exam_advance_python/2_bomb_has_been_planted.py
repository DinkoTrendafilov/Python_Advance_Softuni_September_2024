dimensions = input().split(", ")
rows = int(dimensions[0])
cols = int(dimensions[1])

matrix = []
contra_terrorist_position = ()

for row in range(rows):
    current_row = list(input())
    matrix.append(current_row)
    if "C" in current_row:
        contra_terrorist_position = (row, current_row.index("C"))

ct_row, ct_col = contra_terrorist_position

time_remaining = 16
bomb_defuse_time = 0
bomb_defused = False
game_over = False

while time_remaining > 0 and not game_over:
    command = input()
    if command == "up":
        if ct_row > 0:
            ct_row -= 1
        time_remaining -= 1
    elif command == "down":
        if ct_row < rows - 1:
            ct_row += 1
        time_remaining -= 1
    elif command == "left":
        if ct_col > 0:
            ct_col -= 1
        time_remaining -= 1
    elif command == "right":
        if ct_col < cols - 1:
            ct_col += 1
        time_remaining -= 1
    elif command == "defuse":
        if matrix[ct_row][ct_col] == "B":
            bomb_defuse_time = 4
            time_remaining -= bomb_defuse_time
            if time_remaining >= 0:
                matrix[ct_row][ct_col] = "D"
                bomb_defused = True
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {time_remaining} second/s remaining.")
                game_over = True
                break
            else:
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {abs(time_remaining)} second/s.")
                if matrix[ct_row][ct_col] == "B":
                    matrix[ct_row][ct_col] = "X"
                for row in matrix:
                    print("".join(row))
                game_over = True
                exit()

        else:
            time_remaining -= 2

    if matrix[ct_row][ct_col] == "T":
        matrix[ct_row][ct_col] = "*"
        print("Terrorists win!")
        for row in matrix:
            print("".join(row))
        game_over = True
        exit()

if time_remaining <= 0 and not game_over:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {bomb_defuse_time} second/s.")

for row in matrix:
    print("".join(row))
