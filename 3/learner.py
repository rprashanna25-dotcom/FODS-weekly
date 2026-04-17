"""
this program creates a learner class
it keeps basic information about a learner
the user provides all necessary inputs
an object is initialized using those inputs
finally it prints the learner information
"""

class Learner:
    """
    class used to model a learner with essential details
    """

    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        """
        set up learner attributes
        """
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    def derails(self):
        """
        show learner details in a proper format
        """
        print("\nlearner details")
        print("-" * 30)
        print(f"roll no: {self.roll_no}")
        print(f"full name: {self.full_name}")
        print(f"address: {self.address}")
        print(f"enrollment year: {self.enrollment_year}")
        print(f"program: {self.program}")
        print(f"group: {self.group}")


# take input from user
roll_no = input("enter roll number: ")
full_name = input("enter full name: ")
address = input("enter address: ")
enrollment_year = input("enter enrollment year: ")
program = input("enter program: ")
group = input("enter group: ")

# create learner object
learner = Learner(roll_no, full_name, address, enrollment_year, program, group)

# display details
learner.derails()