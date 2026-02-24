# tuple_count.py

numbers = tuple(map(int, input().split()))
element = int(input())

count = 0
for num in numbers:
    if num == element:
        count += 1

print(count)