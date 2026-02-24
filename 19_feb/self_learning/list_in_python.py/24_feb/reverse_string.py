# reverse_string.py

text = input()
reverse = ""

for char in text:
    reverse = char + reverse

print(reverse)