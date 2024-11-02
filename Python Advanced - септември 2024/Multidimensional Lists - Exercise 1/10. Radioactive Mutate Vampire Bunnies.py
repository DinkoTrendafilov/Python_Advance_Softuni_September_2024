num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number: "))

result = num1 / num2
result1 = num1 // num2
result2 = num1 % num2

print(f"{num1} /  {num2} = {result} -- Count symbols: {len(str(result))}")
print(f"{num1} // {num2} = {result1}")
print(f"{num1} %  {num2} = {result2}")
