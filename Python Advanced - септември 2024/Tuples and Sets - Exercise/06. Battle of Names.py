n = int(input())

odd_sum = set()
even_sum = set()

for i in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(char) for char in name) // i

    if ascii_sum % 2 == 0:
        even_sum.add(ascii_sum)
    else:
        odd_sum.add(ascii_sum)

result = ""
if sum(odd_sum) > sum(even_sum):
    result = odd_sum - even_sum

elif sum(odd_sum) < sum(even_sum):
    result = odd_sum ^ even_sum

else:
    result = odd_sum | even_sum

print(*result, sep=", ")
