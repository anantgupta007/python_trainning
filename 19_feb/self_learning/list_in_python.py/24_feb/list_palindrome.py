# list_palindrome.py

numbers = list(map(int, input().split()))

if numbers == numbers[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")