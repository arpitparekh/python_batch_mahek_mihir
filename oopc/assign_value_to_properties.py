class Vehicle:
  name = ""
  model = ""
  no = 0

  def assign(self,n,m,number):
    self.name = n
    self.model = m
    self.no = number
    
  def display(self):
    print("Name : ",self.name)
    print("Model : ",self.model)
    print("Number : ",self.no)

v= Vehicle()

v.assign("BMW","X5",1234)

v1 = Vehicle()
v1.assign("Audi","Q7",1234)

v.name = "Alto"
v.display()
v1.display()
