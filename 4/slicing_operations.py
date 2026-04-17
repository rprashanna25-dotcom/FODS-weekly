"""
program accepts a list of numbers from the user.
it sorts the list and applies slicing operations.
"""

def handle_list(nums):
    # sort list
    nums.sort()

    print("sorted list:", nums)
    print("index 3 to 6:", nums[3:7])
    print("index 6 to 9:", nums[6:10])
    print("index 4 to 10:", nums[4:11])


def main():
    nums = list(map(int, input("enter at least 12 numbers: ").split()))

    if len(nums) < 12:
        print("please enter at least 12 numbers")
    else:
        handle_list(nums)


if __name__ == "__main__":
    main()