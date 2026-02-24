# check_palindrome.py

s = input()

reverse = ""
for char in s:
    reverse = char + reverse

if s == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")