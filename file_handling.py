# creating, reading, updating, and deleting files

# open()

# write a file

# path = "/home/arpit-parekh/files/test.txt"
# file = open(path,"w")  # if not then create else replace
# file.write("Bascom Bridge")
# file.close()

# download image and store in inside a files folder
image_path = "https://t3.ftcdn.net/jpg/02/99/04/20/360_F_299042079_vGBD7wIlSeNl7vOevWHiL93G4koMM967.jpg"

# virtual environment

import requests as rq
image = rq.get(image_path)

path = "/home/arpit-parekh/files/my_image.jpg"
file = open(path,"wb")
file.write(image.content)

file.close()

# read a file
path = "/home/arpit-parekh/files/test.txt"
file = open(path,"r")
print(file.read())

# remove a file
import os
os.remove(path)
print("File Removed")
