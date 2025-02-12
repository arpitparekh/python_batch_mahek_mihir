# Write a program to find the first and last digit of a number.

num = int(input("Enter a number : "))  # 1234

last_digit = num%10
print("Last digit :",last_digit)

"""
1234
1234//10 = 123
123 % 10 = 3
123//10 = 12
12 % 10 = 2
12//10 = 1
1 % 10 = 1
"""

ld = 0

while num!=0:   # 1234
  ld = num%10   # 4  # 3
  num = num//10 # 123 # 12

print("First digit :",ld)


