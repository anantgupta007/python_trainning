# armstrong_number.py

num = int(input())
temp = num
sum = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")