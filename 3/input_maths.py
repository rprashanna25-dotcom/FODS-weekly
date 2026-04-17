"""
this program accepts a list of integers from the user
it carries out addition subtraction multiplication and division
the results are recorded in a file along with the current date and time
it continues running until the user enters exit
after exiting it displays all stored results in a neat format
"""


import datetime

# file name to store results
file_name = "math_results.dat"

# open file in append mode
file = open(file_name, "a")

while True:
    # take list of integers from user
    nums = input("enter integers separated by space or type exit: ")

    # check exit condition
    if nums.lower() == "exit":
        break

    # convert input into list of integers
    try:
        num_list = list(map(int, nums.split()))
    except:
        print("invalid input try again")
        continue

    # check if list has at least two numbers
    if len(num_list) < 2:
        print("enter at least two numbers")
        continue

    # perform operations
    addition = sum(num_list)

    subtraction = num_list[0]
    for n in num_list[1:]:
        subtraction -= n

    multiplication = 1
    for n in num_list:
        multiplication *= n

    division = num_list[0]
    try:
        for n in num_list[1:]:
            division /= n
    except ZeroDivisionError:
        division = "undefined"

    # get current date and time
    now = datetime.datetime.now()

    # write results to file
    file.write(f"\n{now}\n")
    file.write(f"numbers: {num_list}\n")
    file.write(f"addition: {addition}\n")
    file.write(f"subtraction: {subtraction}\n")
    file.write(f"multiplication: {multiplication}\n")
    file.write(f"division: {division}\n")
    file.write("*" * 35 + "\n")

# close file after loop ends
file.close()

# display file content in formatted way
print("\n saved results \n")
print("=" * 35)
with open(file_name, "r") as file:
    print(file.read())