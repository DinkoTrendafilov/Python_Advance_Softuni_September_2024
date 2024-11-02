from collections import deque

food_portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
peaks_copy = peaks.copy()
day = 0
while food_portions and stamina:
    day += 1
    if day > 7:
        break
    current_food = food_portions.pop()
    current_stamina = stamina.popleft()

    result = current_food + current_stamina

    key_to_remove = None
    for key, value in peaks_copy.items():
        if result >= value:
            key_to_remove = key
            del peaks_copy[key_to_remove]
            break
        else:
            break

    if not peaks_copy:
        break

if peaks_copy:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print("Conquered peaks:")
    for peak, portion in peaks.items():
        print(peak)
