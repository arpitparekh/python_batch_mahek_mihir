# 12
"""
12 * 1 = 12
12 * 2 = 24
12 * 3 = 36
12 * 4 = 48
12 * 5 = 60
12 * 6 = 72
12 * 7 = 84
12 * 8 = 96
12 * 9 = 108
12 * 10 = 120
"""

num = int(input("Enter a number : "))  # 12

for i in range(1,11):
  # print(num,"*",i,"=",num*i)
  print(f"{num} * {i} = {num*i}")


# fstring
value = 12
print("Value is :",value)
print(f"Value is {value}")
