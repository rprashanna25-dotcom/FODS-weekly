# Function to sort names in reverse alphabetical order
def sort_names_reverse(names):
    return sorted(names, reverse=True)

# List of names
students = ["Aman", "Prashanna", "Gita", "Bikash"]

result = sort_names_reverse(students)
print("Sorted Names (Reverse Alphabetical):", result)