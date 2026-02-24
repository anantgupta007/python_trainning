# palindrome_string.py

def is_palindrome(text):
    return text == text[::-1]

text = input()

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")