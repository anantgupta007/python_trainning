# tuple_unique.py

numbers = tuple(map(int, input().split()))

if len(numbers) == len(set(numbers)):
    print("Unique")
else:
    print("Not Unique")