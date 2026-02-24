# rotate_list.py

numbers = list(map(int, input().split()))
k = int(input())

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print(*rotated)