n = int(input())

matrix = []

for _ in range(n):
    row = list(input())
    matrix.append(row)

searched_symbol = input()
position = None

for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] == searched_symbol:
            position = (row_index, col_index)
            break
    if position:
        break

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")
