def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    attempts = 0

    while left <= right:

        mid = (left + right) // 2
        attempts += 1

        if arr[mid] == target:
            print(f"Числото {target:_} е намерено на индекс {mid:_} след {attempts:_} опита.")
            return mid

        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    print(f"Числото {target} не е намерено след {attempts} опита.")
    return -1


n = int(input("Enter range of numbers: "))
goal_number = int(input("Enter target number: "))

sorted_list = [x for x in range(1, n + 1)]

binary_search(sorted_list, goal_number)
