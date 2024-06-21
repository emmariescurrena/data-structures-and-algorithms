# pylint: disable=import-error
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules..."""
import os
import pandas as pd


def clear():
    """Clear terminal"""

    os.system("cls" if os.name == "nt" else "clear")


def ask_again():
    """Ask to search again"""

    answer = input("Insert another name to search. Else, insert '0': ")
    return answer


def search_person_number():
    """Search a person and prints her number"""

    # Ask name to search
    search = ""
    while True:
        clear()
        if search != "":

            search = search.capitalize()
            # Import names's list
            df = pd.read_csv("list.csv")

            # Search and print person's number
            while True:

                df_half = len(df)//2
                index = df.index[0] + df_half
                name = df["Name"][index]
                print(name)

                if name == search:
                    number = df["Number"][index]
                    print(f"{name} no.: {number}")
                    break

                elif len(df) == 1:
                    print("Person not found")
                    break

                elif name < search:  # Keep above half
                    df = df[df_half:]
                else:
                    df = df[:df_half]  # Keep below half

        search = input("\nInsert 0 to exit\n\nEnter name to search: ")
        if search == "0":
            quit()


search_person_number()
