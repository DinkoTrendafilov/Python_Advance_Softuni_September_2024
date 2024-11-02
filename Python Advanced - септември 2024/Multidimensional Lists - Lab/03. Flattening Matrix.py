n = int(input())

matrix = []
flat_matrix = []

for row in range(n):
    row_input = input().split(", ")
    row_int = [int(num) for num in row_input]
    matrix.append(row_int)
    flat_matrix.extend(row_int)

print(flat_matrix)
