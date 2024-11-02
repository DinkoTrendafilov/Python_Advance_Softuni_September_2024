from collections import deque

kids = deque(input().split())
turns = int(input())

while len(kids) > 1:
    kids.rotate((turns - 1))
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")
