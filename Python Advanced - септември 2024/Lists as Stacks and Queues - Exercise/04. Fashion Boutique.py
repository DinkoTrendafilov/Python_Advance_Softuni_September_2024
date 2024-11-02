box_clothes = [int(el) for el in input().split()]
rack_capacity = int(input())

racks_counter = 1
current_rack_space = rack_capacity

while box_clothes:
    cloth = box_clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks_counter += 1
        current_rack_space = rack_capacity - cloth

print(racks_counter)
