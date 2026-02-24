# replace_vowels.py

s = input()
vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print(result)