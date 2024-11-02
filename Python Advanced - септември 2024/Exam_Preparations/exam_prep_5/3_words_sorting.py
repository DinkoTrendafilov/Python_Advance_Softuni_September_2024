def words_sorting(*words):
    d = {}
    result = ""

    for word in words:
        word_value = sum([ord(ch) for ch in word])
        d[word] = word_value

    if sum(d.values()) % 2 == 1:
        d = dict(sorted(d.items(), key=lambda kvp: (-kvp[1])))
    else:
        d = dict(sorted(d.items(), key=lambda kvp: (kvp[0])))

    for (key, value) in d.items():
        result += f"{key} - {value}\n"

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
