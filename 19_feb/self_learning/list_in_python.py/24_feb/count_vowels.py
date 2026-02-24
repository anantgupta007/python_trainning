# count_vowels.py

text = input()
count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print(count)