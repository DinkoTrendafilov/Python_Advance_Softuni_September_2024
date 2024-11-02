row_count, col_count = [int(num) for num in input().split()]

matrix = []
sub_matrix = []
max_sum = float("-inf")

for row in range(row_count):
    row_data = [int(num) for num in input().split()]
    matrix.append(row_data)

for row_index in range(row_count - 2):
    for col_index in range(col_count - 2):

        first_row = matrix[row_index][col_index:col_index + 3]
        second_row = matrix[row_index + 1][col_index:col_index + 3]
        third_row = matrix[row_index + 2][col_index:col_index + 3]

        sum_elements = sum(first_row) + sum(second_row) + sum(third_row)

        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in sub_matrix]
