# prime number
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

num= int(input("Enter a number : "))  # 31  # 2..30

flag = True

for i  in range(2,num):
  if num%i==0:
    flag = False
    break

if flag:
  print("Number is prime")
else:
  print("Number is not prime")
