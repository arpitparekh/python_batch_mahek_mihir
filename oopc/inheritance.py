# inheritance
# varso
# when one class uses  the properties and functions of another class

class Person:
  name = ""
  age = 0

  def walking():
    print("Person is walking")

class Student(Person):
  pass

s = Student()

# single inheritance

class A:  # parent class # base class # super class
  def fun1(self):
    print("This is fun1")

class B(A): # child class #  derived class # sub class
  def fun2(self):
    print("This is fun2")

b = B()
b.fun1()
b.fun2()

# multi level

class P:
  def fun1(self):
    print("This is fun1")

class Q(P):
  def fun2(self):
    print("This is fun2")

class R(Q):
  def fun3(self):
    print("This is fun3")


r = R()
r.fun1()
r.fun2()
r.fun3()

# mutiple inheritance

class P1:
  def fun1(self):
    print("This is fun1")

class P2:
  def fun2(self):
    print("This is fun2")

class Q1(P1,P2):
  def fun3(self):
    print("This is fun3")


# heirarchical inheritance
class A:
  def fun1(self):
    print("This is fun1")

class B(A):
  def fun2(self):
    print("This is fun2")

class C(A):
  def fun3(self):
    print("This is fun3")
