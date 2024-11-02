from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque([int(x) for x in input().split()])
needed_quantity = deque([int(x) for x in input().split()])

max_initial_fuel = len(initial_fuel)
counter = 0

while initial_fuel and additional_consumption_index:
    fuel = initial_fuel[-1]
    index = additional_consumption_index[0]
    current_needed_quantity = needed_quantity[0]

    result = fuel - index

    if result >= current_needed_quantity:
        counter += 1
        initial_fuel.pop()
        additional_consumption_index.popleft()
        needed_quantity.popleft()
        print(f"John has reached: Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter + 1}")
        break

if max_initial_fuel > counter and counter:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([f'Altitude {num}' for num in range(1, counter + 1)])}")
if max_initial_fuel > counter and not counter:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
if max_initial_fuel == counter:
    print("John has reached all the altitudes and managed to reach the top!")
