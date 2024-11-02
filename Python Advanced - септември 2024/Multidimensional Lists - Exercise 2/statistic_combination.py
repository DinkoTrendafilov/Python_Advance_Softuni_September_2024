import math

needed_percent = float(input("Enter rainy possibility % : "))
number_of_days = int(input("Enter number of days: "))

res_needed_percent = (needed_percent) / 100
other_needed_percent = (1 - res_needed_percent)
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

for (key, value) in sorted_dictionary.items():
    print(f"Rainy days: {key} || Times: {value} || {(value * 100):.2f} %")
