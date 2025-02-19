# constrcutor
# constructor is a special method that is used to intialize the object
# constructor calls automatically when object is created
# __init__() is a python constructor

class Student:

  def __init__(self):                   # constructor
    print("This is constructor")

  def fun(self):
    print("This is fun")

s = Student()
s.fun()

#######################################################################################

class Admin:
  name = ""
  age = 0


  def __init__(self,n,a):
    self.name = n
    self.age = a
  def display(self):
    print("Name : ",self.name)
    print("Age : ",self.age)

a = Admin("Raj",20)
a.display()


##################################################################################

class Circle:
  radius = 0.0

  def __init__(self,r):
    self.radius = r

  def area(self):
    return 3.14*self.radius*self.radius

  def circumference(self):  # પરિઘ
    return 2*3.14*self.radius

c= Circle(10)
print("Area : ",c.area())
print("Circumference : ",c.circumference())
