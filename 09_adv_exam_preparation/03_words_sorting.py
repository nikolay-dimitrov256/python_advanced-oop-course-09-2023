def words_sorting(*words):
    words_dict = {}
    result = []

    for word in words:
        words_dict[word] = sum(ord(ch) for ch in word)

    if sum(words_dict.values()) % 2 == 1:
        words_dict = dict(sorted(words_dict.items(), key=lambda kvp: -kvp[1]))
    else:
        words_dict = dict(sorted(words_dict.items(), key=lambda kvp: kvp[0]))

    for key, value in words_dict.items():
        result.append(f"{key} - {value}")

    return "\n".join(result)


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
