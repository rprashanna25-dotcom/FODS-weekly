# Function for addition
def add (a,b):
    return a + b
# Function for multiplication
def product (a,b):
    return a * b
# Function for Division
def divide (a,b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    # Function for floor division
def floor_divide (a,b):
    if b != 0:
        return a // b
    else:
        return "Cannot divide by zero"
    # Function for exponentiation
def exponent (a,b):
    return a ** b
# Taking input form user
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

# For diaplaying result
print("\n--- Results ---")
print("Addition:", add(num1, num2))
print("Multiplication:", product(num1, num2))
print("Division:", divide(num1, num2))
print("Floor Division:", floor_divide(num1, num2))
print("Exponentiation:", exponent(num1, num2))