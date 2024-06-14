# Arithmetic operators - perform Simple  calculations

num1=56
num2=8

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2) #modulus operator returns the remainder after dividing 2 numbers

#comparison operators -Compare values.

print (num1<num2)
print (num1>num2)
print (num1<=num2)# less than or equal to
print (num1>=num2)#greater than or equal to
print (num1 ==num2) #equal to
print (num1 !=num2) #not equal to

#Assignment Operators- Assign values to variables

a=200
print(a)
a +=20   #assignment happens first before the  arithmetic operation
print(a)

#logic operatiors :and,not,or

x=100
print(x < 250 and x > 1000)
print(x < 250 or x > 1000)
print (not(x<250 or x>1000))

#Operator precedence -order in which operations get executed
output=(100-4*3/1)
print(output)
print (int(output))

#assignment is to write a simple python program that returns the area of a trapezium
sidea=200
sideb=100
sideh=45
area=(1/2*(sidea+sideb)*sideh)
print(area)

#Conditional statements
temperature =46
if temperature <25:
    print("it is cold ")
elif temperature >25:
    print("it is hot")
else:
    print("Normal temperature")

#A simple program to return  the largest number among three numbers
first=90
second=45
third=69
if  first> second and  first > third :
    print(first,"is the largest number")
elif second >first and second> third :
    print(second,"is the largest number")
else :
    print(third,"is the largest number")

#A program that checks whether a number is even or odd
number=0
if number==0:
    print(number,"is neutral")
elif number%2==0 :
    print(number,"is even")
else :
    print(number,"is odd")





