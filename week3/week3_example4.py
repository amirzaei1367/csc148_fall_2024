def square(a):
    #print("square of ", a, "is ", a*a)
    c = a * a
    print("square of ", a, "is ", c)

def power_3(a):
    c = a * a * a
    print("power_3 of ", a, "is ", c)

def power_4(a):
    c = a * a * a * a
    print("power_4 of ", a, "is ", c)

def power(num, exp):
    c = num ** exp
    print("power ", exp, " of ", num, 'is ', c)

number = float(input("what is the number you want to find its power?"))
exp = float(input("what is exponent?"))
power(number, exp)
power(number, exp)
power(number, exp)
power(number, exp)

