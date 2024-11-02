a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"{'-' * 113}")
print(a)
print(b)
print(f"{'-' * 113}")
print(a.union(b))  # Equivalent to a | b           {1, 2, 3, 4, 5, 6}      d = a | b
print(a.intersection(b))  # Equivalent to a & b    {3, 4}                  c = a & b
print(a.issubset(b))  # Equivalent to a <= b       False
print(a.issuperset(b))  # Equivalent to a >= b     False
print(a.difference(b))  # Equivalent to a - b      {1, 2}                  e = a - b
print(a.symmetric_difference(b))                 # {1, 2, 5, 6}            g = a ^ b
print(f"{'-' * 113}")


