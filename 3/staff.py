"""
This program creates a Staff class to manage staff information
It allows users to enter multiple staff records
The data is stored in a CSV file
It uses try-except blocks to handle file-related errors
Users can also view all the saved staff records
"""

import csv

class Staff:
    """
     To represent a staff member
    """

    def __init__(self, emp_id, full_name, address, phone_number, marital_status, dependents, salary):
        """
        initialize staff attributes
        """
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary

    def to_list(self):
        """
        convert object data into list for csv writing
        """
        return [
            self.emp_id,
            self.full_name,
            self.address,
            self.phone_number,
            self.marital_status,
            self.dependents,
            self.salary
        ]

file_name = "staff.csv"

# function to add staff
def create_staff():
    try:
        # take input
        emp_id = input("enter employee id: ")
        full_name = input("enter full name: ")
        address = input("enter address: ")
        phone_number = input("enter phone number: ")
        marital_status = input("enter marital status: ")
        dependents = input("enter number of dependents: ")
        salary = input("enter salary: ")

        # create object
        staff_member = Staff(emp_id, full_name, address, phone_number, marital_status, dependents, salary)

        # write to csv file
        with open(file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)

            # write data row
            writer.writerow(staff_member.to_list())

        print("staff added successfully")

    except Exception as e:
        print("error while adding staff:", e)

# function for viewing staff
def show_staff():
    try:
        with open(file_name, "r") as csvfile:
            reader = csv.reader(csvfile)

            print("\nstaff records")
            print("_" * 60)

            for row in reader:
                print(f"id: {row[0]}")
                print(f"name: {row[1]}")
                print(f"address: {row[2]}")
                print(f"phone: {row[3]}")
                print(f"marital status: {row[4]}")
                print(f"dependents: {row[5]}")
                print(f"salary: {row[6]}")
                print("-" * 60)

    except FileNotFoundError:
        print("no staff file found")
    except Exception as e:
        print("error while reading file:", e)


# main loop
while True:
    print("\n1 add staff")
    print("2 view staff")
    print("3 exit")

    choice = input("enter choice: ")

    if choice == "1":
        create_staff()
    elif choice == "2":
        show_staff()
    elif choice == "3":
        break
    else:
        print("invalid choice")