"""
this program transfers data from one file to another
the user provides the source and destination file names
it uses try except blocks for error handling
it displays an error if the input file is missing
it also notifies if the output file already exists
"""

# take file names from user
input_file = input("enter input file name: ")
output_file = input("enter output file name: ")

try:
    # try opening input file in read mode
    with open(input_file, "r") as f:
        data = f.read()

    # check if output file already exists
    try:
        with open(output_file, "x") as f:
            # write data into new file
            f.write(data)
        print("file copied successfully")

    except FileExistsError:
        print("output file already exists")

except FileNotFoundError:
    print("input file does not exist")