names = input().split()

heroes = {}
while True:
    command = input()
    if command == "End":
        break
    name, item, costs = command.split("-")
    costs = int(costs)

    if name not in heroes:
        heroes[name] = {"items": [], "total_cost": 0}

    if item not in heroes[name]["items"]:
        heroes[name]["items"].append(item)
        heroes[name]["total_cost"] += costs

for (name, values) in heroes.items():
    print(f"{name} -> Items: {len(values)}, Cost: {values["total_cost"]}")
