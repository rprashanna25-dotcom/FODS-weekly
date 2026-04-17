'''This program creates a Staff class to manage staff information.
It allows users to enter multiple staff records.
The data is stored in a CSV file.
It uses try-except blocks to handle file-related errors.
Users can also view all the saved staff records.'''
import csv 

def read_file():
    try:
        with open('records.csv' , newline='') as csvfile:
            spamreader = csv.DictReader(csvfile, skipinitialspace=True)
            print(f"{'Name':<15} {'Roll':<10} {'Program':<20} {'Year':<10} {'Group'}")
            print("*" * 66)
            for row in spamreader:
                print(f"{row['student_name']:<15} {row['roll_no']:<10} {row['program']:<20} {row['year']:<10} {row['group']}")
    except FileNotFoundError:
        print("File not found")
if __name__=="__main__":
    read_file()