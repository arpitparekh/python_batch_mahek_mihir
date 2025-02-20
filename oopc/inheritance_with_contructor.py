class College:
  def __init__(self,name,address):
    self.name = name
    self.address = address

  def display(self):
    print("College Name : ",self.name)
    print("Address : ",self.address)

class Student(College):
  def __init__(self,roll,age,name,address):
    # passing data from child class constructor to parent class constructor
    super().__init__(name,address)   # call parent class constructor
    self.roll = roll
    self.age = age

  def display(self):
    print("Roll : ",self.roll)
    print("Age : ",self.age)
    print("College Name : ",self.name)
    print("Address : ",self.address)


# child class constuctor always class parent class constuctor
s = Student(101,20,"ADIT","Anand")
s.display()

s = Student(102,21,"SEPT","Anand")
s.display()
