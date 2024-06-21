# pylint: disable=import-error
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules"""
import time
import pandas as pd


def main():
    """Order array by selection"""

    df = pd.read_csv("disordered_numbers.csv")
    arr = df.loc[:, "Numbers"]

    tic = time.perf_counter()

    for min_index in range(len(arr)):
        for index in range(len(arr)-min_index-1):
            if arr[index] > arr[index+1]:
                temp = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = temp

    toc = time.perf_counter()
    print(f"\nSorted in {toc - tic:0.4f} seconds")

    arr.to_csv("sorted_bubble.csv", index=False)

    quit()


main()
