def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}
    result = ""

    for name, status in args:
        if status:
            successful_emperors[name] = 0
        else:
            unsuccessful_emperors[name] = 0

    for name, years in kwargs.items():
        if name in successful_emperors:
            successful_emperors[name] += years
        else:
            unsuccessful_emperors[name] += years

    sorted_successful_emperors = dict(sorted(successful_emperors.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    sorted_unsuccessful_emperors = dict(sorted(unsuccessful_emperors.items(), key=lambda kvp: (kvp[1], kvp[0])))

    result += f"Total number of emperors: {len(sorted_successful_emperors) + len(sorted_unsuccessful_emperors)}\n"
    if sorted_successful_emperors:
        result += "Successful emperors:\n"
        for name, years in sorted_successful_emperors.items():
            result += f"****{name}: {years}\n"

    if unsuccessful_emperors:
        result += "Unsuccessful emperors:\n"
        for name, years in sorted_unsuccessful_emperors.items():
            result += f"****{name}: {years}\n"

    return result


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14, ))
print(f"{'-' * 113}")
print(list_roman_emperors(("Augustus", True),
                          ("Trajan", True),
                          ("Nero", False),
                          ("Caligula", False),
                          ("Pertinax", False),
                          ("Vespasian", True),
                          Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19, ))
print(f"{'-' * 113}")
print(list_roman_emperors(("Augustus", True),
                          ("Trajan", True),
                          ("Claudius", True), Augustus=40, Trajan=19, Claudius=13, ))
print(f"{'-' * 113}")
