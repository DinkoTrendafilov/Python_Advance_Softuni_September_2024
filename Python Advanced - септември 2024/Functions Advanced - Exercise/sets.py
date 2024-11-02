a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a & b     # 3, 4
f = a ^ b     # 1, 2, 5, 6
u = a | b     # 1, 2, 3, 4, 5, 6
e = a - b     # 1, 2
g = b - a     # 5, 6


print(c)
print(f)
print(u)
print(e)
print(g)


