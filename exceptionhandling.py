#exception is just an error in python
try:
    print(x)
except:
    print("An error occurred")

finally:
    print("success")

num1=67
num2=0
try:
    print(num1/num2)
except :
        print("ZeroDivisionError")
finally:
        print("success")