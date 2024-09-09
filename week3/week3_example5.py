"ax^2+bx+c=0"

def quadEquation(a,b,c):
    x1 = (-b + ((b**2 - 4 * a * c) ** 0.5)) / (2 * a)
    x2 = (-b + ((b**2 - 4 * a * c) ** 0.5)) / (2 * a)

    return x1, x2

a1, a2 = quadEquation(1,4,4)

print("sum of the solutions are", a1 + a2)
