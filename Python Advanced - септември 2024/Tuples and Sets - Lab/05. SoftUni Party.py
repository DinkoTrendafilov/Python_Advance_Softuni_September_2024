n = int(input())
reservations = set()

for _ in range(n):
    reservation = input()
    reservations.add(reservation)

while True:
    guest = input()
    if guest == "END":
        break
    if guest in reservations:
        reservations.remove(guest)

print(len(reservations))
for guest in sorted(reservations):
    print(guest)
