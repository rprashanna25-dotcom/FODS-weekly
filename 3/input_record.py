import csv

"""
this program defines a function to add student records
it takes input details from the user
the data is stored in a csv file
it writes headers if the file is empty
finally it confirms that the record is saved
"""

def record():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll No: ")
    prg = input("Enter program: ")
    year = input("Enter Year: ")
    grp = input("Enter Group: ")

    records_field = ['student_name', 'roll_no', 'program', 'year', 'group']

    with open('records.csv','a', newline='') as csvfile:  
        writer = csv.DictWriter(csvfile, fieldnames=records_field)    
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'student_name': name, 'roll_no': roll, 
            'program': prg, 'year': year, 'group': grp
        })        
    print("Record added successfully.")

if __name__ == "__main__":
    record()