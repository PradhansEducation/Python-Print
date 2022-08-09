# type() function to get type of any data
print(type(10))
print(type(10.5))
print(type(8))
print(type(8.0))

a=56
print(a, 'has a type ', type(a))

b=56.48
print(b, 'has a type ', type(b))

c=5+6j
print(c, 'has a type ', type(c))

# boolean data type
print(True, 'has a type ', type(True))
print(False, 'has a type ', type(False))

a=True
b=False
print(a)
print(b)

# Python string
print("Hello World", "has a type ", type("Hello World"))
print('Hello World', "has a type ", type('Hello World'))
print('word', "has a type ", type('word'))
print('a', "has a type ", type('a'))
print('@', "has a type ", type('@'))
print('25', "has a type ", type('25'))

a = "25"
print(a, "has a type ", type("25"))
b = 25
print(b, "has a type ", type(b)) # anything within '__' or "__" is treated as string.

# Python list
a = [2, "Hello", True, 100, 2]
print(a)
print(a, "has a type ", type(a))

# Python Tupple
a = (2, "Hello", True, 100, 2)
print(a)
print(a, "has a type ", type(a))

# Python Dictionary
fruit = {'mango':40, 'banana':10, "cherry":20}
print(fruit)
print(fruit, 'has a type ', type(fruit))

# Python Set
a = {1, 2, 3}
print(a)
print(a, "has a type ", type(a))

# Type Conversion
# Python int()
print(int(4.6))
print(int(True))
print(int(False))
print(int(10))
# print(int("Hello")) will show error as it has non numeric value

#Python Float
print(float(45))
print(float(True))
print(float(False))
print(float(10))
# print(float("Hello")) will show error as it has string

# Python string str()
a = str(45)
print(a)
print(type(a))
print(str(45))
print(str(4.5))
print(str(True))
print(str([1, 2, 3, 4]))
print(str({'a':'1', 'b':'2'}))

# Python Bool()
print(bool(0.5))
print(bool(True))
print(bool(False))
print(bool(0.0))
print(bool(None))
print(bool("Hello"))
print(bool([]))

# Python Type() and Python isinstance()
print(type(10))
print(isinstance(3, int))

a = 3
print(isinstance(a, float))
b = "Python"
print(isinstance(b, str))
c = True
print(isinstance(c, bool))