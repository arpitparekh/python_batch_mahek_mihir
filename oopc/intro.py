# oopc
# object oriented programming concept

# class
class Student:
  # class attribute # class variables
  # class methods # class function
  # class is a template
  name = ""
  dob = ""
  height = 0.0

  def learning(self):
    print("Student is learning")

# objects are used to access class properties and methods

s = Student()
s.name = "Mit"
s.dob = "12/12/2000"
s.height = 5.6
s.learning()
print(s.name)
print(s.dob)
print(s.height)

s1  = Student()
s1.name = "Raj"
s1.dob = "12/12/2000"
s1.height = 5.6
s1.learning()
print(s1.name)
print(s1.dob)
print(s1.height)
