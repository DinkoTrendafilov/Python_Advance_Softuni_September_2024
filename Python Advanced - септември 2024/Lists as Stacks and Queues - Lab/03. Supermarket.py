from collections import deque

dec = deque()

while True:
    name = input()
    if name == "End":
        break
    elif name == "Paid":
        while dec:
            print(dec.popleft())
        dec = deque()
    else:
        dec.append(name)

print(f"{len(dec)} people remaining.")
