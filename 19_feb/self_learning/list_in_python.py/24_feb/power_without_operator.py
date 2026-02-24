# power_without_operator.py

base = int(input())
exponent = int(input())

result = 1

for i in range(exponent):
    result *= base

print(result)