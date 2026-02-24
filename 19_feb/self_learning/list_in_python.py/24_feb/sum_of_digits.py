# sum_of_digits.py

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input())
print(sum_digits(num))