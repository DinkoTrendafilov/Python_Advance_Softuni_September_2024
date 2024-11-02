n = int(input())

matrix = []

for row in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)

while True:
    command = input()
    if command == "END":
        break
    split_command = command.split()
    action = split_command[0]
    r = int(split_command[1])
    c = int(split_command[2])
    value = int(split_command[3])

    if (r not in range(n)) or (c not in range(n)):
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[r][c] += value

    elif action == "Subtract":
        matrix[r][c] -= value

[print(*row) for row in matrix]
