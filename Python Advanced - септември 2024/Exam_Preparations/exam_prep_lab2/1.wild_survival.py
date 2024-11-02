from collections import deque

bee_groups = deque([int(x) for x in input().split()])
bee_eaters_groups = [int(x) for x in input().split()]

bee_eater_killed_bee = 7

while bee_groups and bee_eaters_groups:
    current_bees = bee_groups.popleft()
    current_bee_eaters = bee_eaters_groups.pop()

    while current_bees > 0 and current_bee_eaters > 0:
        current_bees -= bee_eater_killed_bee
        if current_bees >= 0:
            current_bee_eaters -= 1

    if current_bees > 0:
        bee_groups.append(current_bees)
    elif current_bee_eaters > 0:
        bee_eaters_groups.append(current_bee_eaters)

print("The final battle is over!")

if not bee_eaters_groups and not bee_groups:
    print("But no one made it out alive!")
elif bee_eaters_groups and not bee_groups:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters_groups))}")
elif bee_groups and not bee_eaters_groups:
    print(f"Bee groups left: {', '.join(map(str, bee_groups))}")
