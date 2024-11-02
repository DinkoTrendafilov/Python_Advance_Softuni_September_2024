ave = float(input("Enter your needed average result: "))

dictionary = {
    "Dinko": [129, 45, 67, 22, 60, 23, 24, 25, 99, 97],
    "Anna": [49, 33, 44, 55, 300, 110],
    "Ivan": [316, 200, 19, 56, 0, 0, 0, 0, 0, 0, 0],
    "Qna": [44, 33, 32, 11, 100, 371],
    "Mihail": [31, 88, 77, 65, 24, 57, 81, 72, 96],
    "Iliana": [45, 91, 44, 111, 89, 56, 78, 44, 33]
}

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kvp: (abs(sum(kvp[1]) / len(kvp[1]) - ave), kvp[0])))

print()
for key, values in sorted_dictionary.items():
    result = sorted(values, reverse=True)
    avg = sum(result) / len(result)
    diff = abs(avg - ave)
    print(f"{key}  --->  {' '.join(str(x) for x in result)} ---> "
          f"Sum of elements: {(sum(result)):_} -- {len(result)} -- AVG: {avg:.2f} -- DIFF: {diff:.2f}")
print()
