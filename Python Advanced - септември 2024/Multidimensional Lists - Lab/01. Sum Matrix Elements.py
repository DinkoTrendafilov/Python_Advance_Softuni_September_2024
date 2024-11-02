row_count, col_count = [int(num) for num in input().split(", ")]

matrix = []

for row in range(row_count):
    row_data = [int(num) for num in input().split(", ")]
    matrix.append(row_data)

sum_matrix = sum([sum(inner_list) for inner_list in matrix])
print(sum_matrix)
print(matrix)
