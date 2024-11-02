a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6}
print(*a)
a.difference_update(b)
print(*a)
a.update(b)
print(*a)
