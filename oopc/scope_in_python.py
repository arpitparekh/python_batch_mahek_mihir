a = 20  # global scope

def maru_function():  # local scope
  # a = 40
  global a
  a = a + 10
  print(a)

maru_function()


# function inside a function
def outerFunction():
  print("Outer Function")
  a = 10
  def innerFunction():
    print(a)
    print("Inner Function")
  return innerFunction

outerFunction()()


