row_count = int(input())

matrix = []
even_matrix = []

for _ in range(row_count):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

for row in matrix:
    even_numbers = [num for num in row if num % 2 == 0]
    even_matrix.append(even_numbers)

print(even_matrix)
