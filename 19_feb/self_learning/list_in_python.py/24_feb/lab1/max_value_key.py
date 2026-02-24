# max_value_key.py

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

max_key = max(d, key=d.get)

print(max_key)