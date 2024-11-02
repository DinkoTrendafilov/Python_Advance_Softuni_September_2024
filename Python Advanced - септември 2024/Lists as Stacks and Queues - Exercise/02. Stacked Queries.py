n = int(input())

stack = []

for _ in range(n):
    split_command = input().split()
    number_one = int(split_command[0])

    if number_one == 1:
        number_two = int(split_command[1])
        stack.append(number_two)

    elif number_one == 2:
        if stack:
            stack.pop()

    elif number_one == 3:
        if stack:
            print(max(stack))

    elif number_one == 4:
        if stack:
            print(min(stack))

stack.reverse()
print(*stack, sep=", ")
