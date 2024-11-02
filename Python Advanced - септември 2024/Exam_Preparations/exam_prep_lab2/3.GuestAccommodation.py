def accommodate(*guests, **rooms):
    sorted_rooms = sorted(rooms.items(), key=lambda kvp: (
        kvp[1], int(kvp[0].split('_')[1])))
    accomodations = {}
    unsuccessfully_accommodated_guests = 0

    for guest in guests:
        accommodated = False
        for room in sorted_rooms:
            room_name, room_capacity = room
            if room_capacity >= guest:
                accomodations[int(room_name.split('_')[1])] = guest
                sorted_rooms.remove(room)
                accommodated = True
                break
        if not accommodated:
            unsuccessfully_accommodated_guests += guest

    result = []
    if accomodations:
        result.append(f"A total of {len(accomodations)} accommodations were completed!")
        for room_number, guest_count in sorted(accomodations.items()):
            result.append(f"<Room {room_number} accommodates {guest_count} guests>")
    else:
        result.append("No accommodations were completed!")

    if unsuccessfully_accommodated_guests:
        result.append(f"Guests with no accommodation: {unsuccessfully_accommodated_guests}")

    if sorted_rooms:
        result.append(f"Empty rooms: {len(sorted_rooms)}")

    return "\n".join(result)


print(f"{'-' * 113}")
print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(f"{'-' * 113}")
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(f"{'-' * 113}")
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
print(f"{'-' * 113}")
