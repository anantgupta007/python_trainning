# set_difference.py

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = set1.difference(set2)

print(*result)