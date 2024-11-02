import requests

city_name = input("Enter a city name: ")
print(city_name)

print(f"Display Weather report for: {city_name}")

url = f"https://wttr.in/{city_name}"
response = requests.get(url)

print(response.text)
