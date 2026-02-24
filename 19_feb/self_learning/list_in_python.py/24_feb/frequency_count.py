# frequency_count.py

numbers = list(map(int, input().split()))

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    print(key, ":", freq[key])