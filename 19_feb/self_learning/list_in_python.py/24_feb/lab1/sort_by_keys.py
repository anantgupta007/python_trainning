# sort_by_keys.py

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

sorted_dict = dict(sorted(d.items()))

print(sorted_dict)