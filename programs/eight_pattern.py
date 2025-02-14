"""
*****
"""
for i in range(1,10):
  for j in range(1,6):
    if(j==1 or i==1 or j==5 or i==9 or i==5):
      if (i==1 and j==1 or i==9 and j==5 or i==5 and j==1 or i==5 and j==5 or i==1 and j==5 or i==9 and j==1):
        print(" ",end="")
      else:
        print("*",end="")
    else:
      print(" ",end="")
  print()
