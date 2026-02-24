# greatest_of_four.py

a = float(input())
b = float(input())
c = float(input())
d = float(input())

greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print(greatest)