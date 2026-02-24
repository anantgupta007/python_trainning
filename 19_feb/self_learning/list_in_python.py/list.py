n = 5

# Upper Pyramid
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1))

# Lower Pyramid
for i in range(n-1):
    print(" " * (i+1), end="")
    print("*" * (2*(n-i-2)+1))