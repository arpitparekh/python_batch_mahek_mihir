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
****      i = 2 // j = 4  //
***       i = 3 // j = 3
**        i = 4 // j = 2
*
"""
for i in range(1,6): # 1  # 2 # 3
  for j in range(1,7-i):
    print("*",end="")

  print()

print()

for i in range(1,6): # 1  # 2 # 3
  for j in range(1,7-i):

    if(i==1 or j==1 or j==6-i):
      print("*",end="")
    else:
      print(" ",end="")
  print()

"""  pyramid 1 3 5 7 9

     *
    ***
   *****
  *******
 *********
  i   j
 1 => 1
 2 => 3
 3 => 5
 4 => 7
 5 => 9

 j = i

"""

my_num = int(input("Please Enter No of pyramid : "))  # 4

for i in range(1,6):

  for j in range(1,6-i):  # space
    print(" ",end="")


  for k in range(1,my_num+1):

    for j in range(1,2*i):
      print("*",end="")

  #  1|7  2|5  3|3  4|1

    for j in range(1,11-2*i):  # space
      print(" ",end="")


  print()


"""

    *       *
   ***     ***
  *****   *****
 ******* *******
*****************

"""
