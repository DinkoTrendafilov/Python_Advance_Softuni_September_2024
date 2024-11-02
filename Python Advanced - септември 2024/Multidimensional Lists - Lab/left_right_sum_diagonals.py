n = int(input())

matrix = []
sum_left_diagonal = 0
sum_right_diagonal = 0

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for index in range(n):
    sum_left_diagonal += matrix[index][index]
    sum_right_diagonal += matrix[index][n - 1 - index]

print(f"Sum of left diagonal is: {sum_left_diagonal}")
print(f"Sum of right diagonal is: {sum_right_diagonal}")
