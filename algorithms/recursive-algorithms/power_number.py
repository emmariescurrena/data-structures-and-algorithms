# pylint: disable=bare-except
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules..."""

def get_power(b,e):
    """Get result of number!"""

    if e == 1:
        return b
    elif e == 0:
        return 1
    return b*get_power(b,e-1)


def program():
    """Ask number"""

    base =  int(input("Insert base of the power: "))
    exponent =  int(input("Insert exponent of the power: "))
    print(f"Result is {get_power(base, exponent)}")

    quit()

program()
