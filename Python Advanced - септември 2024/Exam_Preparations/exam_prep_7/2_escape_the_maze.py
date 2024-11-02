n = int(input())
health = 100
matrix = []
player_position = ()

movements = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(n):
    current_row = list(input())
    matrix.append(current_row)
    if "P" in current_row:
        player_position = (row, current_row.index("P"))

prow, pcol = player_position

while True:
    move = input()

    if not (0 <= prow + movements[move][0] < n and 0 <= pcol + movements[move][1] < n):
        continue

    matrix[prow][pcol] = "-"
    prow += movements[move][0]
    pcol += movements[move][1]

    element = matrix[prow][pcol]

    if element == "X":
        print("Player escaped the maze. Danger passed!")
        matrix[prow][pcol] = "P"
        break

    elif element == "H":
        health = min(100, health + 15)

    elif element == "M":
        health -= 40
        if health <= 0:
            health = 0
            print("Player is dead. Maze over!")
            matrix[prow][pcol] = "P"
            break

    matrix[prow][pcol] = "P"

print(f"Player's health: {health} units")
for row in matrix:
    print("".join(row))
