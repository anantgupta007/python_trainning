# min_in_tuple.py

numbers = tuple(map(int, input().split()))

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print(minimum)