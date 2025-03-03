class Student:

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def __str__(self):   # string representation of an object
    return f"Name: {self.name}, Age: {self.age}"

s = Student("Sumit",23)
print(s)

