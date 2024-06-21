# pylint: disable=bare-except
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules..."""
import time
import sys

sys.setrecursionlimit(20000)

def get_factorial(number):
    """Get result of number!"""

    if number == 1:
        return 1
    else:
        return number*get_factorial(number-1)

def program():
    """Ask number"""

    number =  int(input("Insert an integer number <= 0 to get factorial: "))
    if number > 0:
        tic = time.perf_counter()
        print(f"The factorial of {number} is {get_factorial(number)}")
        toc = time.perf_counter()
        print(f"\nOrdered in {toc - tic:0.4f} seconds")

program()
