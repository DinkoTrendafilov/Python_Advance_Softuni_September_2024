def even_odd(*args):
    command = args[-1]
    if command == "even":
        even_numbers = [x for x in args[:-1] if x % 2 == 0]
        return even_numbers
    elif command == "odd":
        odd_numbers = [x for x in args[:-1] if x % 2 != 0]
        return odd_numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
