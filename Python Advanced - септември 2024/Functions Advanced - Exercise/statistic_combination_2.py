import math

n = int(input("Enter number of iterations: "))
print()
total_sum = 0
max_value = float("-inf")
max_element = 0

for element in range(0, n + 1):
    result = math.comb(n, element)
    if result > max_value:
        max_value = result
        max_element = element
    total_sum += result
    print(f"Comb: {element} from {n} = {result:_}")
print()
print(f"Total sum of combinations: {total_sum:_}")
print(f"Maximum combination value: {max_value:_} elements {max_element} from {n}")
print(f"Max value: [{max_value:_}] / Total combinations [{total_sum:_}] = {(max_value / total_sum * 100):.2f} %")
