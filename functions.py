#inbuilt functions/standard library functions
#MIN
y=min(23,56,1000,5647)
print(y)

#MAX FUNCTION
X=max(70,2,45,789)
print("The maximum number is",X)

#this function returns two raised to power three
z=pow(2,3)
print(z)

#user defined functions
def school():
    print("Emobilis")

school() #this is calling a function to call a function u have to mention its name

def multiply():
    num1=5
    num2=6
    print(num1*num2)
multiply()


#PARAMETERS and ARGUMENTS
def add():
    a=5
    b=6
    print(a+b)
add()


def add(a,b):
    print(a+b)
add(5,6)

def Employee(fullname,age,salary,phoneNo,position):
    print(fullname,age,salary,phoneNo,position)
Employee("Job Kamau",45,5000,254745676511,"managing director")
Employee("Joel Ndegwa",35,55000,25476706511,"Sales person")
Employee("Stacy Mutheu",24,34500,254798789451,"Human resource manager")
