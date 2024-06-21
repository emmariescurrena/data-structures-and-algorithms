# pylint: disable=import-error
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules"""
import random
import pandas as pd

def generate_array():
    """Generate disordered array"""

    num = int(input("Insert number: "))

    def rnumber():
        """Returns random"""

        random_number = random.randint(1,num)

        return random_number

    df=pd.DataFrame(dict(Numbers = []))
    row_number = 0

    while row_number != num:

        new_number = rnumber()
        repeated = False
        for n in df.loc[ :, "Numbers"]:
            if n == new_number:
                repeated = True
                break
        if repeated is False:
            df.loc [ row_number, "Numbers"] = new_number
            row_number += 1

    df.Numbers = df.Numbers.astype("int")
    df.to_csv("disordered_numbers.csv", index=False)
    quit()

generate_array()
