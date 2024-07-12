search = input("Enter food: ")
search_var = input(f"Enter {search} characteristic (optional): ")

search = search.capitalize()
if type(search) != str or search == "":
    print("Food required")
    quit()

import csv

with open ("food.csv") as database:
    readdata = csv.reader(database, delimiter = ",")
    replacements = ["Data.", ".", "Vitamins","Major Minerals", "Fat", " - RAE"]
    line_count = 0
    columns_name = []
    column_number = 0
    number_food_variants = 0
    for row in readdata:
        if line_count == 0:
            for column in row:
                if column_number < len(row)-1:
                    columns_name.append(column.replace(f"{replacements[0]}", "").replace(f"{replacements[1]}", "").replace(f"{replacements[2]}", "").replace(f"{replacements[3]}", "").replace(f"{replacements[4]}", "", 1).replace(f"{replacements[5]}", ""))
                    column_number += 1
                else:
                    line_count +=1
                    column_number = 1
                    break
        elif type(search_var) == str and search in row[1] and search_var in row[1]:
            if column_number == 1:
                    print(row[1])
                    column_number += 1
            for property in row:
                if column_number < len(row)-1:
                    print(f"{columns_name[column_number]}: {row[column_number]}")
                    column_number += 1
                else:
                    print(" ")
                    number_food_variants += 1
                    line_count += 1
                    column_number = 1
                    break       
        elif search_var == False and search in row[1]:
            if column_number == 1:
                    print(row[1])
                    column_number += 1
            for property in row:
                if column_number < len(row)-1:
                    print(f"{columns_name[column_number]}: {row[column_number]}")
                    column_number += 1
                else:
                    print(" ")
                    number_food_variants += 1
                    line_count += 1
                    column_number = 1
                    break
        elif row[0] != search and number_food_variants > 0:
            print(f"{number_food_variants} variants founded")
            break
        else:
            line_count += 1

print(line_count)