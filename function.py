# def function(name,age):
#     print(name,' \n',age)

# name = input("Enter your name: ")
# age = int(input("Enter you age:"))

# function(name,age)


# def func1(*args):
#     for i in args:
#         print(i)


# func1(20,40,80)
# print()
# func1(80,100)


# def calculation(a,b):
#     return a+b,a-b
    
# add,sub = calculation(40,10)
# print(add,sub)



def show_employee(name,salary):
    if salary>100000:
        print("The name of employee is:",name," and salary is: ",salary)
    else:
        print("The name of employee is:",name," and salary is: ",9000)


name = input("Enter the name of employee:")
salary = int(input("Enter the salary:"))

show_employee(name,salary)