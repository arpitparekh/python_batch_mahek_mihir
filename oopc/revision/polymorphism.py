"""
variables
datatypes
operators
conditional statements
loops
loop inside loop
functions
oopc
class object
constructor
inheritance super().__init()

"""

# polymorphism
# poly = many
# morphism = form

# functtional polymorphism
# class polymorphism

list = [1,2,3,4,5,6,7,8,9,0]
name = "Bascom"

print(len(list))  # duble dholki
print(len(name))

# args and kwargs



# args function

def marufunction(*args):  # args store all the parameters into tuple
  sum =0
  for i in args:
    sum = sum+i
  print(sum)

marufunction(1,2,3)
marufunction(1,2,3,4,5,6,7,8,9,0)
# marufunction("Hello",True,454.54545)


# kwargs function  # keyword argument functions

def taruFuntion(**kwargs):
  print(kwargs)

taruFuntion(name="Bascom",age =20,address="Ahmedabad")
taruFuntion(name="Bascom",age =20,address="Ahmedabad",phone=9876543210,email="EMAIL@gmail.com")


def sum(a,b):
  print(a+b)

sum(10,20)
sum("Hello","World")
sum([1,2],[3,4])


# class polymorphism
class A:
  def fun1(self):
    print("This is fun1 A")

class B(A):
  def fun1(self):
    super().fun1()  # calling parent class function from child class


b = B()
b.fun1()
