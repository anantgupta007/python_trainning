# safe_remove_key.py

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

remove_key = input()

# Safely remove
d.pop(remove_key, None)

print(d)