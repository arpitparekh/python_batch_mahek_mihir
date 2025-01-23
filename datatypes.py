# interpreted

# variables
a = 12

# a = variable name
# 12 variable
# 12 values is assigning to varaible name a

# datatypes
# types of values that we are storing in variables

# int
a : int = 12
print(a)

a = 13   # re-assignment
print(a)

num = 56
print(type(num))

# float
a = 12.56
print(type(a))

# bool
isLogin = True
print(type(isLogin))

# complex
complex_num = 12+3j
print(type(complex_num))

"""
String Types: str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range ,	set, frozenset
Mapping Type: 	dict
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType
"""

name = "Hello"
address = 'ahmedabad'
print(type(name))
print(type(address))
# welcome "Student"

print(' Welcome"Student" ')

g = None  # empty variable
print(type(g))

g = 12
print(type(g))

g = "Hello"
print(type(g))

# sequence types
# list # dynamic array
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)
print(type(fruits))

values = [12,12.34,"Hello", True,12+13j]
print(values)

# tuple
# immutable datatype
studentNames = ("Sumit", "Raj", "Raju", "Rajesh",12,12.34,True)
print(studentNames)
print(type(studentNames))

# set
# unordered # unique values
countries = {"india", "usa", "uk", "japan","india","usa"}
print(countries)
print(type(countries))

# dictionary
# key value pair
student = {"name":"Pradip",
           "age":23,
           "isLogin":True,
           "name":"Bhaijan"}
print(student)

data = {12:12.34,True:"Hello",12+13j:"Hello"}
print(data)


# range datatype
_bascom = range(1,11)   # if else and loop
print(_bascom)
