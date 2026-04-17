"""
program performs operations on matrices
it checks dimension compatibility before carrying out calculations
"""

import numpy as np

def create_matrix_from_input(rows, cols):
    #ensures correct number of elements per row
    matrix = []

    for i in range(rows):
        row = list(map(int, input().split()))

        if len(row) != cols:
            raise ValueError("Incorrect number of elements in a row")

        matrix.append(row)

    return np.array(matrix)


def calculate_matrix_results(m1, m2, r1, c1, r2, c2):
    # addition and subtraction
    if m1.shape == m2.shape:
        print("\naddition:\n", m1 + m2)
        print("\nsubtraction:\n", m1 - m2)
    else:
        print("matrices not same size for addition or subtraction")

    # multiplication
    if c1 == r2:
        print("\nmultiplication:\n", np.dot(m1, m2))
    else:
        print("matrices not compatible for multiplication")


def run():
    try:
        r1 = int(input("enter rows of matrix 1: "))
        c1 = int(input("enter cols of matrix 1: "))
        print("enter elements:")
        m1 = create_matrix_from_input(r1, c1)

        r2 = int(input("enter rows of matrix 2: "))
        c2 = int(input("enter cols of matrix 2: "))
        print("enter elements:")
        m2 = create_matrix_from_input(r2, c2)

        calculate_matrix_results(m1, m2, r1, c1, r2, c2)

    except Exception as e:
        print("error:", e)


if __name__ == "__main__":
    run()