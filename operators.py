# operators are the symbols that perform operations on variables and values
# arithmetic operators
# +, -, *, /, %(modulo), **(pow), //(integer division)

a = 10
b = 30

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(type(a/b))
print(a//b)    # integer division

#=> % modulo
# reminder

x = 12345
y = 10

print(x%y)  # 3  # 4  # last digit

p = 12345
q = 10

print(p//q)  # 1234 # integer division to remove last digit

# ** pow

f = 16
g = 16
print(f**g)

# comparision operators
# relational operators
# ==, !=, >, <, >=, <=
# answer in boolean values
# == equality operator

f = 10
g = 12
ans = f<g
print(ans)
print(f>g)
print(f==g)
print(f!=g)
print(f>=g)
print(f<=g)


# logical operators
# and, or, not
# always between 2 realtional  operators
# answer in boolean values

answer = 12 < 10 and 12>10 and 12==12 and 12!=10
answer2  = not(12 < 10 or 12>10 or 12==12 or 12!=10)
print(not answer)
print(answer2)

# not

# no increment and decrement operators in python # ++ --
a = 10

a = a+1  # reassignment

# assignment operators
# = , +=, -=, *=, /=, %=, **=, //=

study = 45
study **= 10
# study = study + 10
print(study)

# is
# is not
