# triangle_type.py

a = float(input())
b = float(input())
c = float(input())

# Check triangle validity
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a Triangle")