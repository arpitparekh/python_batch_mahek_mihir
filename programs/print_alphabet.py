# Write a program to print all alphabets from a to z. - using while loop

i = 97
while i<=122:
  print(chr(i))
  i+=1

character = input("Enter a character: ")  # a , 1 < >  #

if (ord(character)>=97 and ord(character)<=122) or (ord(character)>=65 and ord(character)<=90):
  print("Character is alphabet")
elif ord(character)>=48 and ord(character)<=57:
  print("Character is digit")
else:
  print("Character is symbol")


if character.isalpha():
  print("Character is alphabet")
elif character.isdigit():
  print("Character is digit")
else:
  print("Character is symbol")


