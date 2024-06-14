#While loop
number=25
#incrementing
while number <=30:
    print(number)
    number=number+1

#decrementing a value
count=10

while count>=1:
 print(count)
 count=count-1


#break and continue statements
x=100
while x<=105:
    print(x)
    if x==103:
        break
    x=x+1

#always assign the first value
y=34
while y<= 40 :
    y=y+1
    if y==37:
       continue
    print(y)


#FOR LOOP

for num in range(10):
    print(num)

for z in range(70,80):
    print(z)

#three numbers the third number represents the value in which the numbers are increasing by
for w in range(100,110,4):
    print(w)

languages= ["python","Kotlin","java"]
for lang in languages:
    print(lang)