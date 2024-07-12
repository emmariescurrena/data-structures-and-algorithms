# pylint: disable=line-too-long
# pyright: reportMissingModuleSource=false

"""Modules..."""

import os
from csv import writer
import csv
from itertools import repeat
import secrets
import pandas as pd

r_number = secrets.choice(range(1000000, 9999999))

def clear():
    """System clear"""
    os.system("cls" if os.name == "nt" else "clear")

def pass_randomizer(num, spec, lett):
    """Random password generator"""

    letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
    numbers = "1234568790"
    specials = r"|°!@#·$~&/()=}{][?\¡*¿<>+"

    types = []
    types.extend(repeat(1, num))
    types.extend(repeat(2, spec))
    types.extend(repeat(3, lett))

    password = ""
    while len(types) != 0:
        random_type = secrets.choice(types)
        if random_type == 1:
            password += secrets.choice(numbers)
            types.remove(1)
        elif random_type == 2:
            password += secrets.choice(specials)
            types.remove(2)
        elif random_type == 3:
            password += secrets.choice(letters)
            types.remove(3)

    return password

def check_input(paths, path, condition):
    """Back to modify previous or menu"""

    if path == r_number:
        paths -= 1
        return paths
    
    elif path == "0" or 0:
        paths = 0
        return paths
    
    elif condition is True:
        paths += 1
        return paths
    
    print("\nInvalid character")
    return paths

def create():
    """Create and export new password"""

    paths, numbers, specials, letters = 1, 2, 2, 11

    while True:
        try:
            if paths == 0:
                return "menu"

            while paths == 1:
                site = input("\nInsert 0 to go back to menu\n\nInsert site: ") or r_number

                clear()
                paths = check_input(paths, site, site != "")

            while paths == 2:
                user = input("\nPress Enter without characters to go back to previous step\nInsert 0 to go back to menu\n\nInsert user: ") or r_number
                clear()
                paths = check_input(paths, user, user != "")

            while paths == 3:
                default_or_not = input("\nPress Enter without characters to go back to previous step\nInsert 0 to go back to menu\n\nInsert 1 to set your own parameters\nInsert 2 to generate one password with 15 characters, 2 numbers and 2 special characters\n") or r_number
                clear()
                if default_or_not == "2":
                    numbers, specials, letters = 2, 2, 11
                    paths = 8
                paths = check_input(paths, default_or_not, default_or_not == "1")

            while paths == 4:
                pass_len = int(input("\nPress Enter without characters to go back to previous step\nInsert 0 to go back to menu\n\nInsert password lenght (max 100): ") or r_number)
                clear()
                paths = check_input(paths, pass_len, pass_len > 0 and pass_len <= 100)

            while paths == 5:
                numbers = int(input(f"\nPress Enter without characters to go back to previous step\nInsert 0 to go back to menu\n\nInsert number of numbers (max {pass_len}): ") or r_number)
                clear()
                paths = check_input(paths, numbers, numbers >= 0 and numbers <= pass_len)

            while paths == 6:
                specials = int(input(f"\nPress Enter without characters to go back to previous step\nInsert 0 to go back to menu\n\nInsert number of specials characters (max {pass_len-numbers}): ") or r_number)
                clear()
                paths = check_input(paths, specials, specials >= 0 and specials <= (pass_len - numbers))

            if paths == 7:
                letters = pass_len - numbers - specials
                paths += 1

            while paths == 8:
                password = pass_randomizer(numbers, specials, letters)
                print(f"Password generated: {password}")
                option = input("\nPress Enter without characters to save password\nInsert 1 to re-generate password\nInsert 2 to generate password with another parameters\nInsert 3 to generate password for other user\nInsert 0 to return to main menu\n\r") or "4"
                clear()
                if option == "1":
                    pass
                elif option == "2":
                    paths = 3
                elif option == "3":
                    paths = 1
                elif option == "4":
                    with open('pass.csv', 'a', newline='', encoding='utf-8') as file:
                        writer_object = writer(file)
                        writer_object.writerow([site, user, password])
                        file.close()
                    paths += 1
                elif option == "0":
                    return "menu"

            while paths == 9:
                print("\nPassword exported!")
                option = input("\nPress Enter to generate password for other user\nInsert 0 to return to main menu\n") or "1"
                clear()
                if option == "1":
                    paths = 1
                elif option == "0":
                    return "menu"

        except:
            print("\nInvalid character")
        
def modify_password():
    """Modify existent password"""
    
    state = "select password to modify"
    while state != "menu":

        while state == "select password to modify":
            try:
                df=pd.read_csv ("pass.csv")
                print(df)

                old = input("\nPress Enter without characters to go back to menu\n\nInsert the number of the password you want to modify: ") or r_number
                clear()
                if old == r_number:
                    return "menu"
                old = int(old)
                state = "create new password"
            except:
                print("\nInvalid character")

        paths, numbers, specials, letters = 1, 2, 2, 11

        while state == "create new password":
            try:
                if paths == 0:
                    return "menu"

                while paths == 1:
                    print(f"\nPassword selected\n\n{df.iloc[old]}")
                    default_or_not = input("\nPress Enter without characters to select another password\nInsert 0 to go back to menu\n\nInsert 1 to set your own parameters\nInsert 2 to generate one password with 15 characters, 2 numbers and 2 special characters\n") or r_number
                    clear()                
                    if default_or_not == r_number:
                        state = "select password to modify"
                        paths = 7
                    elif default_or_not == "2":
                        paths = 6
                    paths = check_input(paths, default_or_not, default_or_not == "1")

                while paths == 2:
                    pass_len = int(input("\nPress Enter without characters to go back to previous step\nInsert 0 to select another password\n\nInsert password lenght (max 100): ") or r_number)
                    clear()                
                    paths = check_input(paths, pass_len, pass_len > 0 and pass_len <= 100)

                while paths == 3:
                    numbers = int(input(f"\nPress Enter without characters to go back to previous step\nInsert 0 to select another password\n\nInsert number of numbers (max {pass_len}): ") or r_number)
                    clear()
                    paths = check_input(paths, numbers, numbers >= 0 and numbers <= pass_len)

                while paths == 4:
                    specials = int(input(f"\nPress Enter without characters to go back to previous step\nInsert 0 to select another password\n\nInsert number of specials characters (max {pass_len-numbers}): ") or r_number)
                    clear()
                    paths = check_input(paths, specials, specials >= 0 and specials <= (pass_len - numbers))

                if paths == 5:
                    letters = pass_len - numbers - specials
                    paths += 1

                while paths == 6:
                    new = pass_randomizer(numbers, specials, letters)
                    print(f"Password generated: {new}")
                    option = input("\nInsert 0 to return to main menu\n\nPress Enter without characters to confirm password\nInsert 1 to re-generate password\nInsert 2 to generate password with another parameters\n") or r_number
                    clear()
                    if option == r_number:
                        state = "confirm modify"
                    elif option == "1":
                        pass
                    elif option == "2":
                        paths = 1
                    elif option == "0":
                        return "menu"
                    else:
                        print("\nInvalid character")
            except:
                print("\nInvalid character")

        while state == "confirm modify":
            confirm = input(f"\nPress Enter to go back\nInsert 0 to return to main menu\n\nAre you sure you want to change your password to {new}? Type 'Yes' to confirm: ") or r_number
            clear()
            if confirm == r_number:
                state == "select password to modify"
            elif confirm == "menu":
                return "menu"
            elif confirm == "Yes":
                df.iloc [ old, 2 ] = new
                df.to_csv('pass.csv', index=False)
                state = "after modify password"
            else:
                print("\nInvalid answer")

        while state == "after modify password":
            print("\nPassword changed")
            option = input("\nPress Enter to modify another password\nInsert 0 to return to main menu\n\r") or "1"
            clear()
            if option == "0":
                return "menu"
            elif option == "1":
                state = "select password to modify"
            else:
                print("\nInvalid character")

def modify_user():
    """Modify created passwords"""

    state = "modify user"
    while True: 

        while state == "modify user":
            try:
                df=pd.read_csv ("pass.csv")
                print(df)

                old = input("\nPress Enter without characters to go back to menu\n\nInsert number of the username you want to modify: ") or r_number
                clear()
                if old == r_number:
                    return "menu"
                old = int(old)

                state = "insert new user"
            except:
                pass
            
        while state == "insert new user":
            print(f"\nPassword selected\n\n{df.iloc[old]}")
            new = input("\nPress Enter without characters to go back\nInsert 0 to return to main menu\n\nIntroduce new username: ") or r_number
            clear()
            if new == r_number:
                state = "modify user"
            elif new == "0":
                return "menu"
            else:
                state = "confirm new user"
        
        while state == "confirm new user":
            print(f"\nPassword selected\n\n{df.iloc[old]}")
            confirm = input(f"\nPress Enter without characters to go back\n\nAre you sure you want to change your username to {new}? Type 'Yes' to confirm: ") or r_number
            clear()
            if confirm == r_number:
                state == "insert new user"
            elif confirm == "menu":
                return "menu"
            elif confirm == "Yes":
                df.iloc [ old, 1 ] = new
                df.to_csv('pass.csv', index=False)
                state = "after new user"
            else:
                print("\nInvalid answer\n")

        while state == "after new user":
            print("\nUsername changed")
            option = input("\nPress Enter to modify another username\nInsert 0 to return to main menu\n") or "1"
            clear()
            if option == "0":
                return "menu"
            elif option == "1":
                state = "modify user" 
            else:
                print("\nInvalid character")


def delete_password():
    """Delete created passwords"""

    state = "select password to delete"
    while True:

        while state == "select password to delete":
            try:
                df=pd.read_csv ("pass.csv")

                print(f"\n{df}")
                rows = input("\nPress Enter without characters to go back to menu\n\nInsert the number of the password you want to delete: ") or r_number
                clear()
                rows = int(rows)
                if rows == r_number:
                    return "menu"
                
                state = "confirm delete"
            except:
                pass
        
        while state == "confirm delete":
            print(f"\nPassword selected\n\n{df.iloc[rows]}")
            confirm = input("\nPress Enter to go back\n\nAre you sure you want to delete permanently this password? Type 'Yes' to confirm: ") or r_number
            clear()
            if confirm == r_number:
                state == "select password to delete"
            elif confirm == "Yes":
                df.drop(df.index[[rows]], axis=0, inplace=True)
                df.to_csv('pass.csv', index=False)
                print("\nPassword deleted\n")
                state = "after delete"
            else:
                print("\nInvalid answer\n")

        while state == "after delete":
            option = input("\nPress Enter to delete another password\nInsert 0 to return to main menu\n") or r_number
            clear()
            if option == "0":
                return "menu"
            else:
                state = "select password to delete"

def view():
    """Read passwords"""

    with open('pass.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        next(reader)
        fields = ["Site", "Username", "Password"]
        for row in reader:
            print()
            column_number = 0
            for column in row:
                print(f"{fields[column_number]}: {column}")
                column_number += 1

    while True:
        option = input("\nScroll up to see passwords\n\nPress Enter to return to Main menu\nInsert 0 to exit program\n") or "menu"
        clear()
        if option == "0":
            return "close"
        else:
            return "menu"

def program():
    """Choose view, create, modify or close"""

    print("\nWelcome to Pass Generator")

    state = "menu"
    while state != "close":
        print("\nMain menu")
        option = input("\nPress Enter without characters to view passwords\nInsert 1 to create passwords\nInsert 2 to modify a password\nInsert 3 to modify a user\nInsert 4 to delete a password\nInsert 0 to exit program\n") or r_number
        clear()
        if option == r_number:
            state = view()
        elif option == "1":
            state = create()
        elif option == "2":
            state = modify_password()
        elif option == "3":
            state = modify_user()
        elif option == "4":
            state = delete_password()
        elif option == "0":
            state = "close"

    print("\nThanks for using pass Generator!")
    quit()

clear()
program()
