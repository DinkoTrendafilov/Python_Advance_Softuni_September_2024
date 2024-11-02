row_count, col_count = [int(x) for x in input().split()]

matrix = []
sub_matrix = []
counter = 0

for _ in range(row_count):
    data = [el for el in input().split()]
    matrix.append(data)

for row_index in range(row_count - 1):
    for col_index in range(col_count - 1):
        element_1 = matrix[row_index][col_index]
        element_2 = matrix[row_index][col_index + 1]
        element_3 = matrix[row_index + 1][col_index]
        element_4 = matrix[row_index + 1][col_index + 1]

        if element_1 == element_2 == element_3 == element_4:
            counter += 1

print(counter)
