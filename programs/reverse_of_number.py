# 1234
# 4321
num = int(input("Enter a number : "))  # 1234
copy =  num

# while num!=0:
#   print(num%10, end="")
#   num = num//10  # 123

# check wheather the number is palindrome or not

# num = reverse  # 1234

reverse = 0  # 4  # 43  # 432 # 4321
while num!=0:
  last_digit = num%10 # 4 # 3  # 2  # 1
  reverse = (reverse*10)+last_digit
  num = num//10  # 123  # 12 # 1

if copy == reverse:
  print("Number is palindrome")
else:
  print("Number is not palindrome")
