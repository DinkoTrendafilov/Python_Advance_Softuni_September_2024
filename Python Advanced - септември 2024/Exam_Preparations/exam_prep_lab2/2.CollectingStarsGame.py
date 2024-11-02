n = int(input())

matrix = []
player_position = []
stars = 2

for row in range(n):
    current_row = list(input().split())
    matrix.append(current_row)

    if "P" in current_row:
        player_position = [row, current_row.index("P")]
        matrix[row][current_row.index("P")] = "."

directions_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while 0 < stars < 10:
    command = input()

    next_row = player_position[0] + directions_mapper[command][0]
    next_col = player_position[1] + directions_mapper[command][1]

    if not (next_row in range(n) and next_col in range(n)):
        next_row = 0
        next_col = 0

    if matrix[next_row][next_col] == "*":
        stars += 1
        matrix[next_row][next_col] = "."

    elif matrix[next_row][next_col] == "#":
        stars -= 1
        continue

    player_position = [next_row, next_col]

if stars:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player_position[0]}, {player_position[1]}]")

matrix[player_position[0]][player_position[1]] = "P"

for row in matrix:
    print(" ".join(row))
