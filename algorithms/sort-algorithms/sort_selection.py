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

    for i in range(len(arr)):
        minor = arr[i]
        idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < minor:
                minor = arr[j]
                idx = j
        temp = arr[idx]
        arr[idx] = arr[i]
        arr[i] = temp

    toc = time.perf_counter()
    print(f"\nSorted in {toc - tic:0.4f} seconds")

    arr.to_csv("sorted_selection.csv", index=False)

    quit()


main()
