# exception handling is the way to handle error before they can occure

try :
  path = "/home/arpit-parekh/files/test.txt"
  file = open(path,"r")
  print(file.read())
except:
  print("File not found")

print("Rest of the code.....")

def voting(age):
  if age<18:
    raise FileNotFoundError("You are not eligible to vote")
  else:
    print("You are eligible to vote")

try:
  voting(12)
except:
  print("You are not eligible to vote")
finally:
  print("Finally block")

print("Baki no code.....")


# try...except
# raise
# finally  # calls everytime when exceptoion comes or not

# api calling
# json
# database integration # mysql
# whatsapp
# whatsapp api
# mail integration
# tkinter (desktop application)(gui application)
