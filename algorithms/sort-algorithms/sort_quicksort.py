# pylint: disable=import-error
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules"""
import time
import pandas as pd


def main():
    """Order array by merge"""

    df = pd.read_csv("disordered_numbers.csv")
    numbers = df.loc[:, "Numbers"]
    numbers = numbers.tolist()

    def sort_array(arr):

        if len(arr) == 1:
            return arr

        else:
            j, q, r = 0, 0, len(arr)-1
            while j < r:
                if arr[j] <= arr[r]:
                    temp = arr[q]
                    arr[q] = arr[j]
                    arr[j] = temp
                    q += 1
                j += 1
            temp = arr[q]
            arr[q] = arr[r]
            arr[r] = temp
            if q == 0:
                arr = sort_array(arr)
            else:
                arr = sort_array(arr[:q]) + sort_array(arr[q:])
            return arr

    tic = time.perf_counter()
    numbers = sort_array(numbers)
    toc = time.perf_counter()
    print(f"\nSorted in {toc - tic:0.4f} seconds")

    data = pd.DataFrame(numbers)
    data.to_csv("sorted_quicksort.csv", index=False)

    quit()


main()
