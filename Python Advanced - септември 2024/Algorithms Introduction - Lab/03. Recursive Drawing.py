def recursive_drawing(num):
    if num <= 0:
        return

    print("*" * num)
    recursive_drawing(num - 1)
    print("#" * num)


n = int(input())

recursive_drawing(n)
