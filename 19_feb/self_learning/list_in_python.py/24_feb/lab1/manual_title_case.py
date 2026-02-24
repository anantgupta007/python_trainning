# manual_title_case.py

s = input()
words = s.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "

print(result.strip())