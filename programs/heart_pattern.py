# heart pattern
"""
 heart pattern

 **   **
**** ****   pattern 1

*********   pattern 2
 *******
  *****
   ***
    *

25. Plus Pattern

    +
    +
    +
    +
+++++++++
    +
    +
    +
    +
26. X Pattern


 ***
*   *
*   *
*   *
 ***
*   *
*   *
*   *
 ***


30. Heart Pattern

  *****     *****
 *******   *******
********* *********
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *



"""

for i in range(1,6):

  for j in range(1,6-i):  # space
    print(" ",end="")


  for j in range(1,2*i):
    if i!=1 and i!=2 :
      print("*",end="")

  #  1|7  2|5  3|3  4|1

  for j in range(1,12-2*i):  # space
    print(" ",end="")

  for j in range(1,2*i):
    if i!=1 and i!=2 :
      print("*",end="")

  print()

for i in range(1,11):
  for j in range(1,i+1):
    print(" ",end="")
  for j in range(1,20-(2*i)):
    print("*",end="")
  print()
