# if
# if else
# if else ladder
# relational and logical // is not is
# conditional statements are used to controll the flow of the proram

g = 10

if g<9:
  print("Value is greater then 9")
else:
  print("Value is not greater then 9")

if g<=10 and g>9:
  print("Value is greater then 9 and less then equal to 10")
else:
  print("Value is not greater then 9 and less then equal to 10")

###  if else ladder

marks = 77

if marks>=90:
  print("Grade A")
elif marks<90 and marks>=70:
  print("Grade B")
elif marks<70 and marks>=50:
  print("Grade C")
else:
  print("Grade D")


# programs
# check if the number is odd or not

num = 12
# if num%2==0:
#   print("Even")
# else:
#   print("Odd")

# one liner syntax
print("Even") if num%2==0 else print("Odd")


# check of the number is negetive or positive
k = 0

if k<0:
  print("Number is negetive")
elif k>0:
  print("Number is positive")
else:
  print("Number is zero")


# check if the number is divisible by 3 and 5

value = 43
if value%3==0 and value%5==0:
  print("Number is divisible by 3 and 5")
else:
  print("Number is not divisible by 3 and 5")


# max of 2 numbers

num1 = 122
num2 = 20

if num1>num2:
  print("num1 is greater then num2")
else:
  print("num2 is greater then num1")

# max of 3 numbers

num1 = int(input("Enter Number 1 : "))  # type casting
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

if num1>num2 and num1>num3:
  print("num1 is greater")
elif num2>num3:
  print("num2 is greater")
else:
  print("num3 is greater")


# get string from user
# name = input("Please Enter name : ")  # "1212"
# print(name)

# # get integer from user
# num = int(input("Enter Number : "))
# print(num)
# print(type(num))


# to check datatype
height = 4.5

if height is float:
  print("Height is float")
else:
  print("Height is not float")
