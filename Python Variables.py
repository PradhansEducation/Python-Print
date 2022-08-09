# variable used to store values
# here a is a variable that stores a value of 10
from re import X


a =10
print(a)

#we can change the value of a variable anytime
# declaring a variable count
count = 1
print(count)

# reassigning value to the variable count
count = 'Hello World'
print(count)

# assigning values to multiple variables
a=1
b=2
print(a, b)

a, b = 1, 2
print(a, b)

a = b = 'Blue'
print(a, b)

# python swapping
x = 10
y = 5
x, y = y, x 
print(x)
print(y)

# deleting variables in python
color = 'Blue'
print(color)
del color
# the variable color is deleted so "print(color)" will result error

# memory management in python
a = 10
print(a)
print(id(10))  # printing memory location of value 10
print(id(a))   # printing memory location of value assigned to variable a

a = 10 
b = 20
print(id(a)) # printing memory location pointed by variable a
print(id(b)) # printing memory location pointed by variable b

# pointing two variable to the same memory location
var1 = 10
var2 = var1 
print(id(var1)) # printing memory location pointed by variable 1
print(id(var2)) # printing memory location pointed by variable 2