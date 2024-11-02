countries = input().split(", ")
capitals = input().split(", ")

dictionary = dict(zip(countries, capitals))

# for countries, capitals in dictionary.items():
#     print(f"{countries} -> {capitals}")

print(*[f"{countries} -> {capitals}" for countries, capitals in dictionary.items()], sep='\n')
