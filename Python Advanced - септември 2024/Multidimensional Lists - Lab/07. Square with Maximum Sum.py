row_count, col_count = [int(num) for num in input().split(", ")]

matrix = []
sub_matrix = []
max_sum = float("-inf")

for row in range(row_count):
    row_data = [int(num) for num in input().split(", ")]
    matrix.append(row_data)

for row_index in range(row_count - 1):
    for col_index in range(col_count - 1):

        element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]
        sum_elements = element + next_element + below_element + diagonal_element

        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [[element, next_element], [below_element, diagonal_element]]

for el in sub_matrix:
    print(*el)
print(max_sum)
