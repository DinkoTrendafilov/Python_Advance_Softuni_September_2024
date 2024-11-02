import math

needed_percent = float(input("Enter rainy possibility % : "))
number_of_days = int(input("Enter number of days: "))

res_needed_percent = needed_percent / 100
other_needed_percent = 1 - res_needed_percent
result = 0
dictionary = {}

for day in range(0, number_of_days + 1):
    if day == 0:
        result = res_needed_percent ** number_of_days
    elif day == number_of_days:
        result = other_needed_percent ** number_of_days

    result = ((res_needed_percent ** day) * (other_needed_percent ** (number_of_days - day))
              * (math.comb(number_of_days, day)))

    if day not in dictionary:
        dictionary[day] = result

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kvp: (-kvp[1], kvp[0])))
# sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kvp: (kvp[0], -kvp[1])))

counter_top_5 = 0
res = []
top_5_results = []
for (key, value) in sorted_dictionary.items():
    counter_top_5 += 1
    if counter_top_5 <= 5:
        res.append(value)
        top_5_results.append([key, value])

    print(f"Rainy days: {key} || Times: {value} || {(value * 100):.2f} %")

print()
print(f"Sum of top 5 values is: {(sum(res) * 100):.2f} %")
print()
for (num, value) in top_5_results:
    print(f"Rainy days: {num} || Times: {value} || {(value * 100):.2f} %")
