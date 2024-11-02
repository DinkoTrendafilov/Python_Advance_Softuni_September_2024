from collections import deque

stack = deque(input().split())

while stack:
    print(stack.pop(), end=" ")
