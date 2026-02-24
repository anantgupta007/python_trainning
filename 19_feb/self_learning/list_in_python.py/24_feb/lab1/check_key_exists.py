# check_key_exists.py

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

check_key = input()

if check_key in d:
    print("Key exists")
else:
    print("Key does not exist")