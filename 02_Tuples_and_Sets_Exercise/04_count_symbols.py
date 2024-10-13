occurrences = {}
for character in input():
    occurrences[character] = occurrences.get(character, 0) + 1

for character, occurrence in sorted(occurrences.items()):
    print(f"{character}: {occurrence} time/s")


# второ решение
#
# text = input()
#
# for symbol in sorted(set(text)):
#     print(f"{symbol}: {text.count(symbol)}time/s")
