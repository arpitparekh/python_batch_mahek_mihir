# list
# list is a collection of items
list = [1,2,3,4,5,6]

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])

print(list)


for i in range(5):
  print(list[i])

for i in list:
  print(i)


list.append(7)
print(list)

# list.clear()
# print(list)

copy = list.copy()
print(copy)

copy[6] = 99
print(copy)
print(list)


another_copy = list
print(another_copy)

another_copy[6] = 99
print(another_copy)
print(list)

list.append(1)
list.append(1)
print(list)

print(list.count(1))  # count the number of demo = []

demo = [11,22,33,44,55]

list.extend(demo)
print(list)

print(list.index(99))


list.insert(3,66)
print(list)

list.pop()
print(list)

list.pop(3)
print(list)

list.remove(1)
print(list)

# pop and remove are same

list.reverse()
print(list)

list.sort()
print(list)
