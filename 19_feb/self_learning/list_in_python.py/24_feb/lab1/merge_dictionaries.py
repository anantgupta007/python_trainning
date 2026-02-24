# merge_dictionaries.py

n1 = int(input())
dict1 = {}

for _ in range(n1):
    key, value = input().split()
    dict1[key] = int(value)

n2 = int(input())
dict2 = {}

for _ in range(n2):
    key, value = input().split()
    dict2[key] = int(value)

# Manual merge
for key in dict2:
    dict1[key] = dict2[key]

print(dict1)