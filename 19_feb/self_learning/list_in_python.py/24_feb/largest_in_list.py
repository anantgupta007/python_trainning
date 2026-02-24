# largest_in_list.py

numbers = list(map(int, input().split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)