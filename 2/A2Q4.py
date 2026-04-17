# Function to count occurrences
def count_numbers(lst):
    count_dict = {}

    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] =1

    return count_dict

# Three different list
list1 = [1, 2, 2, 3, 1, 4]
list2 = [5, 5, 5, 6, 7]
list3 = [8, 9, 8, 9, 8, 10]

print("List 1:", list1)
print("Count:", count_numbers(list1))

print("\nList 2:", list2)
print("Count:", count_numbers(list2))

print("\nList 3:", list3)
print("Count:", count_numbers(list3))