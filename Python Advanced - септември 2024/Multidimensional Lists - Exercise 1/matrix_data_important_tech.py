matrix = [
    [91, 29, 31, 34],
    [15, 16, 17, 38],
    [19, 10, 11, 12],
    [13, 14, 15, 16],
]
for row in matrix:
    print(*row)
print()
row_count = len(matrix)
column_count = len(matrix[0])
total_elements = row_count * column_count

for index, row in enumerate(matrix):
    print(f"Row: {index} | {' '.join(str(x) for x in row)} | SUM is: {sum(row)}")

print()
for col_index in range(column_count):
    col_sum = 0
    col_value = []
    for row_index in range(row_count):
        col_sum += matrix[row_index][col_index]
        col_value.append(matrix[row_index][col_index])
    print(f"Column: {col_index} | {' '.join(str(x) for x in col_value)} | SUM is: {col_sum}")

print()
print(f"Row count is: {row_count}")
print(f"Column count is: {column_count}")
print(f"Total elements in the matrix are: {total_elements}")

a = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        a.append(matrix[i][j])

print(*a)
print(sum(a))
print(len(a))
print(sum(a) / len(a))

left_diagonal_sum = 0
left_diagonal_value = []
right_diagonal_sum = 0
right_diagonal_value = []

for index in range(len(matrix)):
    left_diagonal_sum += matrix[index][index]
    left_diagonal_value.append(matrix[index][index])
    right_diagonal_sum += matrix[index][column_count - index - 1]
    right_diagonal_value.append(matrix[index][column_count - index - 1])

print(f"Sum of left diagonal is: {left_diagonal_sum} - VALUE: {' '.join(str(x) for x in left_diagonal_value)}")
print(f"Sum of right diagonal is: {right_diagonal_sum} - VALUE: {' '.join(str(x) for x in right_diagonal_value)}")