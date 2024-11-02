def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int) or (length or width) < 0:
        return f"Enter valid values!"

    def area():
        rectangle_area = length * width
        return rectangle_area

    def perimeter():
        rectangle_perimeter = 2 * (length + width)
        return rectangle_perimeter

    result = f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    return result


print(rectangle(2, 10))
print(rectangle('2', 10))