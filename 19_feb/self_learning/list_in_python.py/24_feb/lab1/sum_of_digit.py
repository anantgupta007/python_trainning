# read number
num=int(input())
sum_digit=0
#calculate sum of digits
while num>3:
    digit=num%10
    sum_digit+=digit
    num//=10
    print(sum_digit)