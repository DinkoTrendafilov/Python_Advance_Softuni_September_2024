def grocery_store(**kwargs):
    products = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -ord(kvp[0][0]), kvp[0]))
    return "\n".join(f"{product}: {quantity}" for product, quantity in products)


print(grocery_store(
    bread=12,
    zip=12,
    onion=12,
    pasta=12,
    eggs=12,
))
print()
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
