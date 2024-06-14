#a calculator program that  can work with four arithmetic signs

def add(v, n):
    return v + n

def subtract(v, n):
    return v - n

def multiply(v, n):
    return v * n

def divide(v, n):
    if n == 0:
        return "Error! Division by zero!"
    else:
        return v/ n

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

