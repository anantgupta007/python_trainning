# validate_login.py

username = input().strip()
password = input().strip()

# Conditions:
# Username at least 5 characters
# Password at least 8 characters
# Password must contain at least one digit

if len(username) >= 5 and len(password) >= 8 and any(char.isdigit() for char in password):
    print("Valid")
else:
    print("Invalid")