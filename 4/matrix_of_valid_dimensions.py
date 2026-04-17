"""
this program generates a random numpy array
it arranges the array in sorted order and converts it into a matrix
"""

import numpy as np

def create_random_matrix():
    arr = np.random.randint(1, 100, 12)
    arr.sort()
    matrix = arr.reshape(3, 4)

    print("original array:", arr)
    print("\nreshaped matrix:")
    print(matrix)


def run():
    create_random_matrix()


if __name__ == "__main__":
    run()