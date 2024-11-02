def shopping_cart(*args):
    shopping_info = {}
    result = ""

    for item in args:
        if item == "Stop":
            break

        shopping_info = {"Dessert": [], "Pizza": [], "Soup": []}
        meal, product = item

        if product not in shopping_info[meal]:
            shopping_info[meal].append(product)

    sorted_shoping_list = dict(sorted(shopping_info.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    if not sorted_shoping_list:
        result += "No products in the cart!\n"
    else:
        for meal, products in sorted_shoping_list.items():
            result += f"{meal}:\n"

            if meal == "Pizza":
                for product in sorted(products)[:4]:
                    result += f" - {product}\n"
            elif meal == "Dessert":
                for product in sorted(products)[:2]:
                    result += f" - {product}\n"
            elif meal == "Soup":
                for product in sorted(products)[:3]:
                    result += f" - {product}\n"

    return result


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
