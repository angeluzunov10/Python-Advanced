from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
word_is_found = False
words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in words.keys():
        words[word] = words[word].replace(current_vowel, "")
        words[word] = words[word].replace(current_consonant, "")

        if words[word] == "":
            print(f"Word found: {word}")
            word_is_found = True
            break

    if word_is_found:
        break


if not word_is_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
