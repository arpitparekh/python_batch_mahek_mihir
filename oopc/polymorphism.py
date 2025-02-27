# polymorphism
# poly = many
# morphism = form

def data(*args):  # args create a tuple
  print(args)

# data function is a polimorph function
data(1,2,4,6,7,8,6,5,4,34,3)
data("Hello",True,1,2,3,4,5,6,7,8,9)
data(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0)

# len function is a polimorph function
print(len("Hello"))
print(len([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]))

# class polimorphism

class A:
  def fun1(self):
    print("This is fun1 A")

class B(A):
  def fun1(self):
    print("This is fun1 B")

b = B()
b.fun1()
