# sum_even_upto_n.py

n = int(input())
i = 1
total = 0

while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print(total)