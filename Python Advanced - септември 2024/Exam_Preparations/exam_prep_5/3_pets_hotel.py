def accommodate_new_pets(capacity, max_weight, *args):
    pets_info = {}
    result = ""

    for pets_type, pets_weight in args:
        if capacity <= 0:
            result += "You did not manage to accommodate all pets!\n"
            break
        if pets_weight > max_weight:
            continue

        capacity -= 1
        if pets_type in pets_info:
            pets_info[pets_type] += 1
        else:
            pets_info[pets_type] = 1

    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += f"Accommodated pets:\n"
    for pets_type, count in sorted(pets_info.items()):
        result += f"{pets_type}: {count}\n"

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print()
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print()
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
