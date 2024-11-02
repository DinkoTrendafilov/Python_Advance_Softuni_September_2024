def boarding_passengers(capacity, *passenger_groups):
    available_capacity = capacity
    boarding_details = {}

    for passengers, program in passenger_groups:

        if passengers <= available_capacity:
            if program not in boarding_details:
                boarding_details[program] = passengers
            else:
                boarding_details[program] += passengers

            available_capacity -= passengers

        if available_capacity == 0:
            break

    sorted_boarding_details = sorted(boarding_details.items(), key=lambda x: (-x[1], x[0]))

    result = "Boarding details by benefit plan:\n"
    for program, count in sorted_boarding_details:
        result += f"## {program}: {count} guests\n"

    total_boarded = sum(boarding_details.values())
    total_passengers = sum(group[0] for group in passenger_groups)

    if total_boarded == total_passengers:
        result += "All passengers are successfully boarded!"
    elif available_capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {available_capacity}."

    return result


print(f"{'-' * 113}")
print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(f"{'-' * 113}")
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'),
                          (15, 'Diamond'),
                          (10, 'Gold')))
print(f"{'-' * 113}")
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'),
                          (31, 'Platinum'),
                          (20, 'Diamond')))
print(f"{'-' * 113}")
