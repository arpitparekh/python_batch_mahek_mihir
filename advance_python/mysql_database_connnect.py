# pip install mysql-connector-python
# 2 types of server local server // remote server
DATABASENAME = "mypython"
HOST = "localhost"
PORT = "3306"
USERNAME = "root"
PASSWORD = "Walden0042$$"

import mysql.connector

database = None

try:
  database = mysql.connector.connect(
  host = HOST,
  user = USERNAME,
  password = PASSWORD,
  database = DATABASENAME,
  port=PORT
)

except Exception as e:
  print("Error =>",e)

print("Database Connected")

# create table ###############################################################3
createTableQuery = "create table if not exists student(id int primary key auto_increment, name varchar(100), age int, address varchar(200))"


cursor = database.cursor()
cursor.execute(createTableQuery)
print("Table Created")

# insert data ###############################################################
# name = input("Enter Name: ")
# age = int(input("Enter Age: "))
# address = input("Enter Address: ")

# insertQuery = f"insert into student(name, age, address) values('{name}',{age}, '{address}')"
# cursor.execute(insertQuery)
# database.commit()
# print("Data Inserted")

# update data ###############################################################
# id = int(input("Enter Id: "))
# address = input("Enter Address: ")

# updateQuery = f"update student set address = '{address}' where  id = {id}"
# cursor.execute(updateQuery)
# database.commit()
# print("Data Updated")

#  delete data ###############################################################
# id = int(input("Enter Id: "))
# deleteQuery = f"delete from student where id = {id}"
# cursor.execute(deleteQuery)
# database.commit()
# print("Data Deleted")

# select data ###############################################################
selectQuery = "select * from student"
cursor.execute(selectQuery)
data =  cursor.fetchall()
print(data)
