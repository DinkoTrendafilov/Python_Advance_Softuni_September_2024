def binary_search(numbers, target_number):
    numbers.sort()
    left = 0
    right = len(numbers) - 1

    while left <= right:

        middle_index = (left + right) // 2

        if numbers[middle_index] == target_number:
            return middle_index

        elif numbers[middle_index] > target_number:
            right = middle_index - 1

        else:
            left = middle_index + 1

    return -1


nums = [int(x) for x in input().split()]
needed_number = int(input())

print(binary_search(nums, needed_number))
