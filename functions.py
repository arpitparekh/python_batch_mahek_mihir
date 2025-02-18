# functions
# varitables
# datatypes
# operators
# conditional statements
# loops
# loops inside loop

# functions
# function is block of code that runs when called its called
# function is used to avoid code duplication
# function is used to make code more readable
# function is used to make code more maintainable

# function is a reusable block of code

# functions
# function name
# function parameters
# function body
# function return type

# no parameter, no return type

def maru_function():   # function defination
  print("this is maru function")
  print("Welcome Student")

maru_function()  # function calling
maru_function()  # function calling
maru_function()  # function calling
maru_function()  # function calling
maru_function()  # function calling

def taru_function():
  a = 10
  b = 20
  c = a+b
  print(c)

taru_function()
taru_function()
taru_function()

# function with parameter but no return type

def greet(name):

  print("Hello",name)

greet("Santosh")
greet("Raju")
greet("Suresh")
greet("Ramesh")

def sum(a,b):
  print(a+b)

sum(10,20)
sum(20,30)
sum(30,40)

def multiply(a,b):
  print(a*b)

multiply(10,20)
multiply(20,30)
multiply(30,40)

# function with return type but no parameter

def apdu_function():  # returns an integer
  return 23

# when function returns soething the whole function becomes a value
print(apdu_function())

result = 100 +  apdu_function()
print(result)

# function with parameter and return type
def sabka_function(a,b):
  return a+b+a+10

print(sabka_function(10,20))

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

print(add( sub(10,20) , sub(20,2) ))


# prime number function
