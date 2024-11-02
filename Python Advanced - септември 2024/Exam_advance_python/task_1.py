from collections import deque

contestants = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()

    if contestant >= pie:
        contestant -= pie

        if contestant > 0:
            contestants.append(contestant)
    else:
        pie -= contestant

        if pies and pie == 1:
            pies[-1] += pie
        else:
            pies.append(pie)

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants))}")

elif not pies and not contestants:
    print("We have a champion!")

elif pies and not contestants:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")
