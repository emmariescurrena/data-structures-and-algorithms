# pylint: disable=import-error
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules"""
import time
import pandas as pd


def main():
    """Order array by insertion"""

    df = pd.read_csv("disordered_numbers.csv")
    numbers = df.loc[:, "Numbers"]

    tic = time.perf_counter()

    for i, n in enumerate(numbers):
        for c in reversed(range(i)):
            if numbers[c] > n:
                numbers[c+1] = numbers[c]
            else:
                numbers[c+1] = n
                break
        if numbers[0] == numbers[1]:
            numbers[0] = n

    toc = time.perf_counter()
    print(f"\nSorted in {toc - tic:0.4f} seconds")

    numbers.to_csv("sorted_insertion.csv", index=False)

    quit()


main()
