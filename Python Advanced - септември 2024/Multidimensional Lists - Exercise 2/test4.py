from functools import reduce

numbers = [3, 15, 2]

result = reduce(lambda x, y: x * y, numbers)

print(result)
