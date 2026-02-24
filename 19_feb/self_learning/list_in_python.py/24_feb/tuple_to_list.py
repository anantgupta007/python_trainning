# tuple_to_list.py

numbers = tuple(map(int, input().split()))

converted = list(numbers)

print(*converted)