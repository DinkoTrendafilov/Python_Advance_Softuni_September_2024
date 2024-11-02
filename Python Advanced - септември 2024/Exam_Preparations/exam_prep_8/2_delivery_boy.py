rows, cols = [int(x) for x in input().split()]

matrix = []
player_position = ()

for row in range(rows):
    current_row = list(input())
    matrix.append(current_row)
    if "B" in current_row:
        player_position = (row, current_row.index("B"))

prow, pcol = player_position

direction_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if not (0 <= prow + direction_mapper[command][0] < cols and 0 <= pcol + direction_mapper[command][1] < cols):
        print("The delivery is late. Order is canceled.")
        break

    matrix[prow][pcol] = "."
    prow += direction_mapper[command][0]
    pcol += direction_mapper[command][1]

    element = matrix[prow][pcol]

    if element == "*":
        continue
    elif element == "A":
        matrix[prow][pcol] = "P"
        print("Pizza is delivered on time! Next order...")
        break
    elif element == "P":
        matrix[prow][pcol] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
        break

    matrix[prow][pcol] = "B"

for row in matrix:
    print("".join(row))
