# sort_by_values.py

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))

print(sorted_dict)