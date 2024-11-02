my_list = [int(el) for el in input().split()]

result = ", ".join(str(el) for el in my_list)
average = sum(my_list) / len(my_list)
len_average_digits = len(str(average))

print(my_list)
print(result)
print()
print(f"Average result is: {average} ==> {average:.2f}  | Sum of elements: {sum(my_list)} | {len(my_list)} elements")
print(len_average_digits)
