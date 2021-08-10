'''
Title: Assignment05 - Lists & Dictionaries
Author: Bryan Mon
Course: IT FDN 110 A Su 21: Foundations Of Programming: Python
ChangeLog: (Who, When, What)
    BryanMon, 08-09-2021, Created Script
    BryanMon, 08-09-2021, Copied RRoot's starter code, reviewed, defined variables, added pseudo-code
    BryanMon, 08-09-2021, Added try clause for reading data to our list table (step 1)
    BryanMon, 08-09-2021, Created selectable menu options (step 2). Added comment breaks to format code for readability
    BryanMon, 08-09-2021, Wrote Step 3 task of listing contents of list_table. Added feature to check for empty list
    BryanMon, 08-09-2021, Created step 4 user input captures. Troubleshot High/Low/Exit constraints. Now working
    BryanMon, 08-09-2021, Added row deletion option in step 5. Tested removal and verified working
    BryanMon, 08-09-2021, Added save-to-file function. Tested with new and existing txt file. Completed script
'''

# Declaring our variables
str_todotxt = "ToDo.txt"  # An object that represents a file
str_data = ""  # A row of text data from the file
dict_row = {}  # A row of data separated into elements of a dictionary {Task,Priority}
list_table = []  # A list that acts as a 'table' of rows
str_userchoice = ""  # user input for menu selection
str_task = ""  # user input for task name
str_priority = ""  # user input for priority of task
objfile = None  # our object variable for working with data written to or read from txt file
empty_file = ""  # variable for checking whether txt file is empty

# -----------------------------------------------
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

print("\nLoading data from ToDo.txt...\n")
try:  # Our try clause to read data from our txt
    objfile = open(str_todotxt, "r")  # open file for read only
    for row in objfile:
        dict_row = row.split(",")
        dict_row = {"Task": dict_row[0], "Priority": dict_row[1].strip()}  # load data into our dictionary
        list_table.append(dict_row)  # append dictionary to a list table
    else:
        objfile.close()  # close txt data file
        print("\nData loaded. Moving to main menu.\n")
except:  # if try fails do the follow:
    print("Unable to read", str_todotxt, ". A common cause is that the txt file may not exist.\n")

# -----------------------------------------------
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    str_userchoice = input("Enter your selection [1 to 5]: \n")  # take menu selection input from user

# -----------------------------------------------
# Step 3 - Show the current items in the table
    if str_userchoice.strip() == '1':
        if not list_table:  # check if the list_table is empty. Do the following if true:
            print("List table is empty, please enter a new item from the menu.")
            continue  # return to main menu
        else:  # if list_table has data, do the follow:
            print("    Task    " + ' | ' + "    Priority    ")  # print our list header
            print("-" * 40)  # format after header
            for dict_row in list_table:  # loop through list_table and print row data
                print(dict_row)  # list the contents of dict_row
                print("-" * 40)  # format after each entry
            continue  # return to main menu

# -----------------------------------------------
# Step 4 - Add a new item to the list/Table
    elif str_userchoice.strip() == '2':
        try:  # Our try block to add a new line of data to our txt file
            # capture user input for task name
            str_task = input("Enter a task you wish to save to the list (Enter 'Exit' to quit): \n")
            if str_task == "exit":  # allows exit out of data entry
                continue

            #  capture user priority level for task
            str_priority = input("Enter the priority level for " + str_task + ". Use 'High' or 'Low' or 'Exit'\n")

            #  conditional to ensure either High or Low priority is used
            if str_priority.lower() == "high" or str_priority.lower() == "low":
                dict_row = {"Task": str_task, "Priority": str_priority.upper()}  # save entries to new list row
                list_table.append(dict_row)  # append to list table

            elif str_priority.lower() == "exit":  # allows exit out of data entry
                continue  # return to main menu

            else:  # If user fails to input high, low, or exit; do the following:
                print("Error, invalid priority option. Please use either 'High' or 'Low'.\n")
                continue  # return to main menu

        except:  # if add new line fails, do the following:
            print("Error, please try again.\n")
            continue  # return to main menu

# -----------------------------------------------
# Step 5 - Remove a new item from the list/Table
    elif str_userchoice.strip() == '3':
        if not list_table:  # check if the list_table is empty. Do the following if true:
            print("List table is empty, returning to main menu.")
            continue  # return to main menu
        else:
            str_data = input("\nPlease enter a Task to remove from the list (Enter 'Exit' to quit): \n")

            if str_data.lower() == "exit":  # allows exit out of data entry
                continue  # return to main menu

            else:
                for dist_row in list_table:  # loop through list_table
                    if dist_row["Task"].lower() == str_data.lower():  # check to see if user input is a task on table
                        list_table.remove(dist_row)  # if found, remove row
                        print("Removed", str_data + '\n')
                        print("    Task    " + ' | ' + "    Priority    ")  # print our list header
                        print("-" * 40)  # format after header
                        for dict_row in list_table:  # loop through list_table and print row data
                            print(dict_row)  # list the contents of dict_row
                            print("-" * 40)  # format after each entry
                        continue
                    else:  # if user input fails to match an entry on table, do the following:
                        print("\nTask not found on table.\n")
                        print("    Task    " + ' | ' + "    Priority    ")  # print our list header
                        print("-" * 40)  # format after header
                        for dict_row in list_table:  # loop through list_table and print row data
                            print(dict_row)  # list the contents of dict_row
                            print("-" * 40)  # format after each entry
                        continue  # return to main menu
            continue

# -----------------------------------------------
# Step 6 - Save Tasks to the ToDo.txt file
    elif str_userchoice.strip() == '4':
        try:  # error handling for writing our list table to the txt file
            objfile = open(str_todotxt, "w")  # open our txt file with write permissions
            for dict_row in list_table:  # loop through list_table
                objfile.write(dict_row["Task"] + ',' + dict_row["Priority"] + '\n')  # write rows to our txt file
            else:
                continue  # return to the main menu
        except:  # failed try except, do the following:
            print("Error saving data to file. Please try again.\n")
            continue  # return to the main menu

# -----------------------------------------------
# Step 7 - Exit program
    elif str_userchoice.strip() == '5':
        print("Ending Program. Please press Enter to exit.\n")
        break  # Exit the program
