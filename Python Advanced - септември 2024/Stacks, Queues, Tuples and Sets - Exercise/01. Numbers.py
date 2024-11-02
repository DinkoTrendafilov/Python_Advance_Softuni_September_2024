first_set = {int(x) for x in input().split()}
second_set = {int(x) for x in input().split()}
n = int(input())

for _ in range(n):
    data = input().split()
    command = data[0] + " " + data[1]
    numbers = [int(x) for x in data[2:]]

    if command == "Add First":
        for num in numbers:
            first_set.add(num)

    elif command == "Add Second":
        for num in numbers:
            second_set.add(num)

    elif command == "Remove First":
        for num in numbers:
            if num in first_set:
                first_set.discard(num)

    elif command == "Remove Second":
        for num in numbers:
            if num in second_set:
                second_set.discard(num)

    elif command == "Check Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

first_set = sorted(first_set)
second_set = sorted(second_set)
print(*first_set, sep=", ")
print(*second_set, sep=", ")



