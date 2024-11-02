from collections import deque

customers = deque()
available_liters = int(input())

while True:
    command = input()
    if command == "Start":
        break
    else:
        customers.append(command)

while True:
    command = input()
    if command == "End":
        break
    elif command.isdigit():
        customer = customers.popleft()
        liters_wanted = int(command)
        if available_liters >= liters_wanted:
            available_liters -= liters_wanted
            print(f"{customer} got water")
        else:
            print(f"{customer} must wait")

    else:
        refill_commands, liters = command.split()
        liters = int(liters)
        available_liters += liters

print(f"{available_liters} liters left")
