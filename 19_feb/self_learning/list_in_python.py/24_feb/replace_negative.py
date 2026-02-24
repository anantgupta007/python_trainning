# replace_negative.py

numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(*numbers)