count = 0

for i in range(1,11):  # 10
  for j in range(1, 11): # 10
      count = count+1
      print("Hello World",count,end=" => ")

print("Hello",end="")
print("World")

num1 = 10
num2 = 20
num3 = 30

print(num1,num2,num3,sep="=>")

# square star pattern
"""
*****
*****
*****
*****
*****

"""

for i in range(1,10): # 6 var

  for j in range(1,10): # 5
    print("*",end="")

  print()

# i row and j column

"""   left align triangle
*
**
***
****
*****
"""
for i in range(1,6): # i = 1 , 2
  for j in range(1,i+1):  # 1..2 , 1..3
    print("*",end="")
  print()

"""   inverted left align triangle
*****
****
***
**
*
"""
for i in range(1,6): # 1  # 2 # 3
  for j in range(1,7-i):
    print("*",end="")

  print()
