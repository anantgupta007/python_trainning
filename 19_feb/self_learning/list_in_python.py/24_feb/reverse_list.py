# reverse_list.py

numbers = list(map(int, input().split()))

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(*reversed_list)