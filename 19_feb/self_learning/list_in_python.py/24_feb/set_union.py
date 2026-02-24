# set_union.py

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = set1.union(set2)

print(*result)