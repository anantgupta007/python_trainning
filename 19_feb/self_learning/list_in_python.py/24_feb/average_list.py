# average_list.py

numbers = list(map(int, input().split()))

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

print(average)