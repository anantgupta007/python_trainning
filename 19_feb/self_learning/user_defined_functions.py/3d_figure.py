#3d_figure

# Cube
def cube(side):
    return side * side * side


# Cuboid
def cuboid(l, b, h):
    return l * b * h


# Cylinder
def cylinder(r, h):
    return 3.14 * r * r * h


# Cone
def cone(r, h):
    return (1/3) * 3.14 * r * r * h


# Sphere
def sphere(r):
    return (4/3) * 3.14 * r * r * r


# Hemisphere
def hemisphere(r):
    return (2/3) * 3.14 * r * r * r

r=float(input("enter the value of r"))
l=float(input("enter the value of l"))
h=float(input("enter the value of h"))
b=float(input("enter the value of b"))

