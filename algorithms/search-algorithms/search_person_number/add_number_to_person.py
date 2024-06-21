"""Modules..."""

import secrets
import pandas as pd


def random_number():
    """Module for generate random number"""

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num1 = secrets.choice(numbers)
    num2 = secrets.choice(numbers)
    num3 = secrets.choice(numbers)
    num4 = secrets.choice(numbers)
    num5 = secrets.choice(numbers)
    num6 = secrets.choice(numbers)
    num7 = secrets.choice(numbers)

    r_number = f"221-{num1}{num2}{num3}-{num4}{num5}{num6}{num7}"

    return r_number


df = pd.read_csv("list.csv")
row_number = 1
for row in range(len(df)):
    new = random_number()
    df.iloc[row, 1] = new
    df.to_csv('list.csv', index=False)
    print(row_number)
    row_number += 1
