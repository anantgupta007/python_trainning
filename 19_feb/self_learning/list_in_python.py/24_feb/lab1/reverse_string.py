# reverse_string.py

s = input()
reverse = ""

for char in s:
    reverse = char + reverse

print(reverse)