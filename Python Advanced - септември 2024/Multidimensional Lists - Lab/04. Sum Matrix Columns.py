row_count, col_count = [int(num) for num in input().split(", ")]

matrix = []

for row in range(row_count):
    row_data = [int(num) for num in input().split()]
    matrix.append(row_data)

for col_index in range(col_count):
    col_sum = 0
    for row_index in range(row_count):
        col_sum += matrix[row_index][col_index]
    print(col_sum)
