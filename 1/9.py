# Menu-driven program to compute sums of positive and negative numbers

# Initialize sums
positive_sum = 0
negative_sum = 0

while True:
    # Display menu
    print("Menu:")
    print("n. Enter a number")
    print("q. Exit")

    # Take user choice
    choice = input("Enter your choice: ")

    if choice == 'n':
        # Take a number input from the user
        num = float(input("Enter a number: "))
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num
    elif choice == 'q':
        break
    else:
        print("Invalid choice! Please try again.")

# Display the results
print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")