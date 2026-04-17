def check_armstrong (str):
    # To convert string to integer
    num = int (str)
    power = len(str)
    
    total = 0
    for digit in str:
        d = int (digit)
        total = total + (d ** power)

        if total == num:
         return "Armstrong Number"
    else:
        return "Not an Armstrong Number"
# Taking input from user
number = input ("Enter a number: ")

result = check_armstrong(number)
print(result)