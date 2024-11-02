from collections import deque

monsters_armor = deque([int(x) for x in input().split(",")])
solders_impact = [int(x) for x in input().split(",")]

total_killed_monsters = 0

while monsters_armor and solders_impact:
    current_armour = monsters_armor.popleft()
    current_strike = solders_impact.pop()

    if current_strike >= current_armour:
        total_killed_monsters += 1
        current_strike -= current_armour
        if solders_impact:
            solders_impact[-1] += current_strike
        elif not solders_impact and current_strike > 0:
            solders_impact.append(current_strike)
    else:
        current_armour -= current_strike
        monsters_armor.append(current_armour)

if not monsters_armor:
    print("All monsters have been killed!")
if not solders_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {total_killed_monsters}")
