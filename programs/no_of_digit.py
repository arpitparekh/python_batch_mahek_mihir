# Write a program to count the number of digits in a number.
# 1234

num = int(input("Enter a number : "))  # 1234


count = 0
while(num!=0):
  num = num//10
  count = count+1

print(count)
