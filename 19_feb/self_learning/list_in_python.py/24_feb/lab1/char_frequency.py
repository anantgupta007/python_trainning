# char_frequency.py

s = input()
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for key in freq:
    print(key, freq[key])