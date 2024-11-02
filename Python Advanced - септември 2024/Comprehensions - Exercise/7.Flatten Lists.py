result = [[el.strip() for el in list_as_string.split()] for list_as_string in input().split("|")[::-1]]

final_result = []
for sublist in result:
    final_result.extend(sublist)

print(*final_result)
