# Function to compute factorial
def factorial(r):
    if r == 0:
        return 1
    else:
        return r * factorial(r - 1)

# input from the user
try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        raise ValueError
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input! Please enter a positive integer.")