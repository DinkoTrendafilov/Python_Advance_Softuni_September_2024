row_count = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(row_count):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

col_count = len(matrix[0])

for index in range(len(matrix)):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][col_count - index - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
