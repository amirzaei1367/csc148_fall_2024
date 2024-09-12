
#calculating the distance between two points
def d_calc(x1, y1=123, x2=1, y2=12):
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return dist

#getting the user inputs
x1 = float(input("what is x1"))
x2 = float(input("what is x2"))
y1 = float(input("what is y1"))
y2 = float(input("what is y2"))

#calling the function
#ans = d_calc(x1, y1, x2)

ans = d_calc()
ans = d_calc(12)
ans = d_calc(12, 12)
ans = d_calc(12, 12, 12, 12)
ans = d_calc(x1=12, y1=1024, x2=10.7, y2=123)
ans = d_calc( x2=10.7, y2=123, x1=12, y1=1024)

#print it out
print("distance of two points", x1, y1, "and", x2, y2, "is", ans)


