# second_largest.py

numbers = list(map(int, input().split()))

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)