n = int(input())

matrix = []
for _ in range(n):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

bombs = input().split()
for bomb in bombs:
    row, col = [int(x) for x in bomb.split(",")]
    bomb_value = matrix[row][col]

    if bomb_value > 0:
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r in range(n) and c in range(n) and matrix[r][c] > 0:
                    matrix[r][c] -= bomb_value

        matrix[row][col] = 0

alive_cells = 0
alive_sum = 0

for row in matrix:
    for value in row:
        if value > 0:
            alive_cells += 1
            alive_sum += value

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sum}")

[print(*row) for row in matrix]
