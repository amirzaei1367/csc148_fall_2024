def square(a):
    #print("square of ", a, "is ", a*a)
    c = a * a
    print("square of ", a, "is ", c)

square(3)
square(12)
square(40)
square(1000)
square(-1)
square(3.4)

number = float(input("what is the number you want to find the square?"))
square(number)
