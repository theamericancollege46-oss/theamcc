import math

print("Equation: Ax^2 + Bx + C")

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C:"))

d = b**2 - 4*a*c   

if d < 0:
    print("The roots are imaginary")
else:
    d1 = math.sqrt(d)
    r1 = (-b + d1) / (2 * a)
    r2 = (-b - d1) / (2 * a)

    print("The first root:", round(r1, 2))
    print("The second root:", round(r2, 2))
