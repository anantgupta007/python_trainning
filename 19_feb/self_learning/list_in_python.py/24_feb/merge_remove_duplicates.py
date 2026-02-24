# merge_remove_duplicates.py

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

merged = list1 + list2
result = []

for num in merged:
    if num not in result:
        result.append(num)

print(*result)