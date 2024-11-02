row_count, col_count = [int(num) for num in input().split()]

matrix = []
sub_matrix = []
max_sum = float("-inf")

for row in range(row_count):
    row_data = [int(num) for num in input().split()]
    matrix.append(row_data)

counter = 0
for row_index in range(row_count - 1):
    for col_index in range(col_count - 1):
        counter += 1

        first_row_elements = matrix[row_index][col_index:col_index + 2]
        second_row_elements = matrix[row_index + 1][col_index:col_index + 2]

        sum_elements = sum(first_row_elements) + sum(second_row_elements)

        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [first_row_elements], [second_row_elements]


for el in sub_matrix:
    print(*el)
print(max_sum)
print("Number of matrices:", counter)
