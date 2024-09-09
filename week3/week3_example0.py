#accessing substring of second item in the fruit list
fruits = ['apple', 'banana', 'cherry']
var1 = fruits[1]
print(var1[2:])

#using negative indexing
var2 = fruits[-2]
print(var2[-4:])

print(fruits[-1])
print(fruits[len(fruits)-1])
#print(fruits[len(fruits)])

var3 = len(fruits)
print("var3 has the value", var3)
print(fruits[len(fruits)-1])

marks = [10,23, 34, 35, 36, 367, 12, 23, 324, 76]
print("length of the marks is: ", len(marks))
marks[1] = 180
print(marks)
marks.append(-123)
print(marks)
marks.insert(2, -555)
print(marks)

marks2 = [6,7,8,7,6,5]
marks.extend(marks2)
print(marks)
