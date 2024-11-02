import random

lower = "abcdefghijklmnopqrstuvwxyz".lower()
upper = "abcdefghijklmnopqrstuvwxyz".upper()
numbers = "0123456789"
symbols = "!@#$%^&*()_+=?><[]"

all_characters = lower + upper + numbers + symbols
length = int(input("Enter a length: "))

password = ''.join(random.sample(all_characters, length))

print("Generated Password:", password)
print(f"Length of all characters: {len(all_characters)}")
