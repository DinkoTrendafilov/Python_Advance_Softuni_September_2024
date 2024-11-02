rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    data = input().split()
    matrix.append(data)

while True:
    command = input().split()

    if command[0] == "END":
        break
    elif command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    else:
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if (row1 and row2 not in range(rows)) or (col1 and col2 not in range(cols)):
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]
