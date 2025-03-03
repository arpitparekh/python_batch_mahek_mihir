# scope
# accesibility

a = 50  # global scope

def dance():
  global a    # is used to access the global variable inside the function
  a = a + 10      # local scope
  print(a)

dance()


# function inside a function
def outerfunction():    # closure function
  print("This is outer function")

  num = 20

  def innerfunction():
    print("This is inner function")
    print(num)

  return innerfunction

# when yuo create a function inside a function then it is called as closure function and outter function must return the inner function


outerfunction()()
