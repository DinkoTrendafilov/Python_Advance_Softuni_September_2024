def calc_sum(numbers, index=0):
    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + calc_sum(numbers, index + 1)


nums = [int(x) for x in input().split()]

print(calc_sum(nums))
