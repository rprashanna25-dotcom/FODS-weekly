"""
this program creates a NumPy array and performs basic computations on it.
it finds the sum, mean, maximum, and minimum values.
"""

import numpy as np

def process_array(arr):
    # calculate values
    total_sum = np.sum(arr)
    mean_value = np.mean(arr)
    max_value = np.max(arr)
    min_value = np.min(arr)

    # display results
    print("array:", arr)
    print("sum:", total_sum)
    print("mean:", mean_value)
    print("max:", max_value)
    print("min:", min_value)


def run():
    arr = np.array([10, 20, 30, 40, 50])
    process_array(arr)


if __name__ == "__main__":
    run()