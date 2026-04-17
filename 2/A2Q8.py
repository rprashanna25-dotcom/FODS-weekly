# Function to remove duplicates and sort the list
def remove_duplicates_sort(lst):
    unique_list = list(set(lst))  # Remove duplicates using set
    unique_list.sort()            # Sort in ascending order
    return unique_list

# For user to input number  
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Convert input to integers

# Calling the function
result = remove_duplicates_sort(numbers)

#  To display result
print("List after removing duplicates and sorting:", result)