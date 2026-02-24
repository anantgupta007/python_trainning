# sum_of_values.py

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

total = sum(d.values())

print(total)