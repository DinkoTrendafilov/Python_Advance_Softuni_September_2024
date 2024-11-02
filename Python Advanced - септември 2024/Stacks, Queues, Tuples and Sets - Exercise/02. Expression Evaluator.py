from collections import deque

expression = input().split()
queue = deque()

for c in expression:
    if c not in "+-*/":
        queue.append(int(c))
    else:
        while len(queue) > 1:
            num_1 = queue.popleft()
            num_2 = queue.popleft()
            if c == "+":
                queue.append(num_1 + num_2)
            elif c == "-":
                queue.append(num_1 - num_2)
            elif c == "*":
                queue.append(num_1 * num_2)
            elif c == "/":
                queue.append(num_1 // num_2)

print(queue.popleft())
