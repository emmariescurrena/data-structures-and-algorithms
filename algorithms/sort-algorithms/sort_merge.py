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
            arr_half = len(arr)//2
            fhalf = sort_array(arr[:arr_half])
            shalf = sort_array(arr[arr_half:])
            o, i, j = 0, 0, 0
            while i < len(fhalf) and j < len(shalf):
                if fhalf[i] < shalf[j]:
                    arr[o] = fhalf[i]
                    i += 1
                else:
                    arr[o] = shalf[j]
                    j += 1
                o += 1
            if i == len(fhalf):
                while j < len(shalf):
                    arr[o] = shalf[j]
                    j += 1
                    o += 1
            else:
                while i < len(fhalf):
                    arr[o] = fhalf[i]
                    i += 1
                    o += 1
            return arr

    tic = time.perf_counter()
    numbers = sort_array(numbers)
    toc = time.perf_counter()
    print(f"\nSorted in {toc - tic:0.4f} seconds")

    data = pd.DataFrame(numbers)
    data.to_csv("sorted_merge.csv", index=False)

    quit()


main()
