def calculate(a,b):
    print("Sum:",a+b)
    print("Difference:",a-b)
    print("Product:",a*b)
    if b != 0:
        print("Quotient:",a / b)
    else:
        print("Quotient: Cannot be divided by Zero")

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
calculate (num1, num2)
    