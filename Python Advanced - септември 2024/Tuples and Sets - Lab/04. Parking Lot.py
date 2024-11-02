n = int(input())

cars = set()

for _ in range(n):
    split_command = input().split(", ")
    action = split_command[0]
    car_number = split_command[1]

    if action == "IN":
        cars.add(car_number)

    elif action == "OUT":
        cars.remove(car_number)

if not cars:
    print("Parking Lot is Empty")
else:
    print(*cars, sep="\n")
