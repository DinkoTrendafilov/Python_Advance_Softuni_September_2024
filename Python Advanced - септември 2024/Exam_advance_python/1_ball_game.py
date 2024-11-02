from collections import deque

strengths = [int(x) for x in input().split()]
accuracies = deque([int(x) for x in input().split()])

goals = 0

while strengths and accuracies:
    current_strength = strengths[-1]
    current_accuracy = accuracies[0]

    result = current_accuracy + current_strength

    if result == 100:
        strengths.pop()
        accuracies.popleft()
        goals += 1

    elif result > 100:
        strengths[-1] -= 10
        accuracies.popleft()
        accuracies.append(current_accuracy)
    else:
        if current_strength < current_accuracy:
            strengths.pop()
        elif current_strength == current_accuracy:
            strengths[-1] += current_strength
            accuracies.popleft()
        else:
            accuracies.popleft()

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")

if goals:
    print(f"Goals scored: {goals}")
if strengths:
    print(f"Strength values left: {', '.join(map(str, strengths))}")
if accuracies:
    print(f"Accuracy values left: {', '.join(map(str, accuracies))}")
