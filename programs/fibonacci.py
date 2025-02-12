# 11235813

num = int(input("Enter a Range : "))  # 6


"""
a = 1
b = 1
c = a+b # 2

a = b  # 1
b = c  # 2
c = a+b # 3

a = b  # 2
b = c  # 3
c = a+b # 5

a = b  # 3
b = c  # 5
c = a+b # 8

a = b  # 5
b = c  # 8
c = a+b # 13

"""


a = 1
b = 1

for i in range(1,num+1):
  print(a)
  c = a+b
  a = b
  b = c

