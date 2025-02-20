class Banking:
  def __init__(self,name,balance,ac_no):
    self.name = name
    self.balance = balance
    self.ac_no = ac_no

  def deposite(self,amount):
    self.balance = self.balance+amount

  def withdraw(self,amount):
    self.balance = self.balance-amount

  def display(self):
    print("Name : ",self.name)
    print("Balance : ",self.balance)
    print("Account Number : ",self.ac_no)


b = Banking("Raj",1000,1234)
b.deposite(1000)
b.withdraw(500)
b.display()

