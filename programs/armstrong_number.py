# armstrong number
# 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 992631

# 153 = 1^3 + 5^3 + 3^3 = 153
# 370 = 3^3 + 7^3 + 0^3 = 370
# 371 = 3^3 + 7^3 + 1^3 = 371
# 407 = 4^3 + 0^3 + 7^3 = 407
# 1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1634

num = int(input("Enter a number : "))
copy = num
another_copy = num

count = 0

while num!=0:
  count = count+1
  num = num//10  # 153

arm = 0

while copy!=0:
  last = copy%10  # 3  # 5  # 1
  arm = arm + (last**count)  # 27 + 125 + 1 = 153
  copy = copy//10

if another_copy == arm:
  print("Number is armstrong")
else:
  print("Number is not armstrong")
