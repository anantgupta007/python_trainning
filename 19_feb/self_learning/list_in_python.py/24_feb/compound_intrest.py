#compound intrest calculator
p=float(input("enter principal amount:"))
r=float(input("enter the rate of intrest:"))
t=float(input("enter the time period "))
n=int(input("enter number of times intrest compounded per year:"))
r=r/10
A=p*(1+r/n)**(n*t)
CI=A-p
print("final amount:" round(A,2))
print("compund intrest:",round(CI,2))
              