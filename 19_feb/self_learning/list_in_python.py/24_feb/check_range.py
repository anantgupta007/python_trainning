# check_range.py

num = float(input())
lower = float(input())
upper = float(input())

if lower <= num <= upper:
    print("Within Range")
else:
    print("Out of Range")