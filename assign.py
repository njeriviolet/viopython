#a simple program to allow the user to enter 4 numbers and choose which of the numbers is the smallest

a=int(input("enter value a"))
b=int(input("enter value b"))
c=int(input("enter value c"))
d=int(input("enter value d"))

if a<b   and a<c and a<d :
    print(a , "is the smallest number")
elif b<a and b<c and b<d :
    print(b, "is the smallest number")
elif c<a  and c<b and c<d :
    print(c, "is the smallest number")
else :
    print(d, "is the smallest number")