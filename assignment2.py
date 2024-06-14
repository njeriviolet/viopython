# a python program to check whether a number is prime

def is_prime(number):
    # Handle cases for numbers less than or equal to 1
    if number <= 1:
        return False

    # Check for numbers 2 and 3 separately
    if number <= 3:
        return True

    # Check for even numbers and numbers divisible by 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check for prime numbers of the form 6k ± 1
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


# Example usage:
num = int(input("enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


