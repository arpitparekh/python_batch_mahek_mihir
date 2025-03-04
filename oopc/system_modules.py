import datetime as dt

current = dt.datetime.now()
print(current)

print(current.strftime("%d %A %Y"))

"""
%a 	Weekday, short version 	Wed
%A 	Weekday, full version 	Wednesday
%w 	Weekday as a number 0-6, 0 is Sunday 	3
%d 	Day of month 01-31 	31
%b 	Month name, short version 	Dec
%B 	Month name, full version 	December
%m 	Month as a number 01-12 	12
%y 	Year, short version, without century 	18
%Y 	Year, full version 	2018
%H 	Hour 00-23 	17
%I 	Hour 00-12 	05
%p 	AM/PM 	PM
%M 	Minute 00-59 	41
%S 	Second 00-59 	08
%f 	Microsecond 000000-999999 	548513
%z 	UTC offset 	+0100
%Z 	Timezone 	CST
%j 	Day number of year 001-366 	365
%U 	Week number of year, Sunday as the first day of week, 00-53 	52
%W 	Week number of year, Monday as the first day of week, 00-53 	52
%c 	Local version of date and time 	Mon Dec 31 17:41:00 2018
%C 	Century 	20
%x 	Local version of date 	12/31/18
%X 	Local version of time 	17:41:00
%% 	A % character 	%
%G 	ISO 8601 year 	2018
%u 	ISO 8601 weekday (1-7) 	1
%V 	ISO 8601 weeknumber (01-53) 	01
"""

import math

# 2^3
print(2**3)

# 64
print(math.sqrt(64))

x = 2.6

print(math.ceil(x))  # 3
print(math.floor(x))  # 2

print(round(x))


# regex give me pattern
pattern = "^[a-zA-Z0-9]+([._-][0-9a-zA-Z]+)*@[a-zA-Z0-9]+([.-][0-9a-zA-Z]+)*\.[a-zA-Z]{2,}$"
email = "arpitparekh9@gmail.com"

import re
if re.match(pattern,email):
  print("Valid Email")
else:
  print("Invalid Email")


# file handling
# try except finally
# threading

# json

import os
print(os.getcwd())
print(os.listdir()) 
