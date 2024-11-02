from collections import deque

worm_size = [int(x) for x in input().split()]
hole_size = deque([int(x) for x in input().split()])

fit_count = 0
total_worm_count = len(worm_size)

while worm_size and hole_size:
    current_worm = worm_size[-1]
    current_hole = hole_size[0]

    if current_worm == current_hole:
        fit_count += 1
        worm_size.pop()
        hole_size.popleft()

    else:
        hole_size.popleft()
        worm_size[-1] -= 3

        if worm_size[-1] <= 0:
            worm_size.pop()

if fit_count:
    print(f"Matches: {fit_count}")
else:
    print("There are no matches.")

if not worm_size and fit_count == total_worm_count:
    print("Every worm found a suitable hole!")
elif not worm_size and fit_count < total_worm_count:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(map(str, worm_size))}")

if not hole_size:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, hole_size))}")
