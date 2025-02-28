# import polymorphism as po
# import scope_of_variable as sv

# # polymorphism is module file
# # named module
# po.marufunction(1,2,3)

# sv.outerfunction()()


from polymorphism import marufunction,taruFuntion
# from polymorphism import *   # import all the functions from polymorphism module

marufunction(1,2,3)
taruFuntion(name="Bascom",age=20)


from scope_of_variable import outerfunction
outerfunction()()
