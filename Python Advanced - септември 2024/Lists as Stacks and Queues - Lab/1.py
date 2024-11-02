new_price = float(input("Enter new price: "))
old_price = float(input("Enter old price: "))

result = ((new_price / old_price) * 100) - 100
res = float(f"{result:.2f}")

print(f"{'-' * 113}")
print(f"Result is: {result:_} %")
print(f"Short result is: {res:_} %")
print(f"Integer length of result is: {len(str(int(result)))} digits")
print(f"Float length of result is: {len(str(result)) - len(str(int(result))) - 1} digits")
print(f"Total length of result is: {len(str(result))} digits")
print(f"{'-' * 113}")
