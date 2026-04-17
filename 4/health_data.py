"""
this program loads data from a csv file and generates scatter plots
it visualizes the relationships among different health variables
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_data(df):
    plt.scatter(df["weight"], df["height"])
    plt.xlabel("weight")
    plt.ylabel("height")
    plt.title("weight vs height")
    plt.show()

    plt.scatter(df["age"], df["weight"])
    plt.xlabel("age")
    plt.ylabel("weight")
    plt.title("age vs weight")
    plt.show()

    plt.scatter(df["height"], df["age"])
    plt.xlabel("height")
    plt.ylabel("age")
    plt.title("height vs age")
    plt.show()

    plt.scatter(df["gender"], df["height"])
    plt.xlabel("gender")
    plt.ylabel("height")
    plt.title("gender vs height")
    plt.show()

    plt.scatter(df["gender"], df["weight"])
    plt.xlabel("gender")
    plt.ylabel("weight")
    plt.title("gender vs weight")
    plt.show()


def run():
    try:
        df = pd.read_csv("health_data.csv")
        plot_data(df)
    except FileNotFoundError:
        print("csv file not found")


if __name__ == "__run__":
    run()