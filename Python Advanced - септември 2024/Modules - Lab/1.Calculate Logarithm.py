from math import log, pi

number = int(input())
base = input()

if base == "natural":
    print(f"{log(number):.2f}")

else:
    print(f"{log(number, int(base)):.2f}")

pi_length = len(str(pi))
print(f"Pi: {pi} --- Length is: {pi_length} digits.")
