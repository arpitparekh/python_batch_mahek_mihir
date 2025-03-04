from collections import Counter,defaultdict

data = ["Bmw","Audi","Mercedes","Toyota","Honda","Suzuki","Honda","Toyota","Suzuki","Toyota"]

count = Counter(data)
print(count)

myData = defaultdict(int)
print(myData)
myData["Name"] = "Bascom"
print(myData)

import time

def my_loop():
  start = time.time()
  for i in range(1,100000):
    print(i)
  end = time.time()
  print(end-start,"seconds")

my_loop()


import csv
path = "/home/arpit-parekh/Downloads/archive(3)/exams.csv"


