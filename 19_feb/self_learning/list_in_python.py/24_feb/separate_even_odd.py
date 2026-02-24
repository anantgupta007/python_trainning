# separate_even_odd.py

numbers = list(map(int, input().split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", *even)
print("Odd:", *odd)