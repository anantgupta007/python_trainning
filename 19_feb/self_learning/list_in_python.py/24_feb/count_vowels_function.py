# count_vowels_function.py

def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

text = input()
print(count_vowels(text))