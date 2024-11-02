from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tools = tools.popleft()
    current_substance = substances.pop()

    result = current_tools * current_substance
    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(current_tools + 1)
        if current_substance - 1 > 0:
            substances.append(current_substance - 1)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if (not substances or not tools) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances:
    print(f"Substances: {', '.join(map(str, substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
