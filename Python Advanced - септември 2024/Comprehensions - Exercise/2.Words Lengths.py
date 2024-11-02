names = input().split(", ")

print(*[f"{word} -> {len(word)}" for word in names], sep=', ')
