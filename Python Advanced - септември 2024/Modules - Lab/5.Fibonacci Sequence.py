while True:
    fibonacci_numbers = []
    command = input()
    if command == "Stop":
        break
    split_command = command.split()
    if split_command[0] + " " + split_command[1] == "Create Sequence":
        count = int(split_command[2])

        old = 0
        new = 1

        while len(fibonacci_numbers) < count:
            fibonacci_numbers.append(old)
            old, new = new, old + new
        print(*fibonacci_numbers)

    elif split_command[0] == "Locate":
        number = split_command[1]
        if number in fibonacci_numbers:
            print(f"The number - {number} is at index {fibonacci_numbers.index(number)}")
        else:
            print(f"The number {number} is not in the sequence")
