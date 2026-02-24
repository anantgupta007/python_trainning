# set_intersection.py

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = set1.intersection(set2)

print(*result)