n = int(input())

matrix = []
sum_diagonal = 0

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for index in range(n):
    sum_diagonal += matrix[index][index]

print(sum_diagonal)
