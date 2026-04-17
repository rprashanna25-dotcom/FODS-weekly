# in take mask of 6 subject  
marks = []
for i in range(6):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# To calculate total, average, and percentage
total = sum(marks)
average = total / 6
percentage = (total / 600) * 100

# determine the grade
if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Distinction"
elif percentage >= 55:
    grade = "Second Distinction"
elif percentage >= 45:
    grade = "Third Distinction"
else:
    grade = "Fail"

# Display 
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")