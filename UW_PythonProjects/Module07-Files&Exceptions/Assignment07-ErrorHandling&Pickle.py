"""
Title: Assignment 07 - Error Handling & Pickle
Description: A fundamentals script for demonstration of Error Handling & Pickling in Python
Author: Bryan Mon
Course: IT FDN 110 A Su 21: Foundations Of Programming: Python
ChangeLog: (Who, When, What)
    BryanMon, 08-22-2021, Created Script
    BryanMon, 08-22-2021, Inserted script pseudo-code
    BryanMon, 08-23-2021, Created menu while loop for user interaction
    BryanMon, 08-23-2021, created two functions, one for reading binary file, the other for overwriting a binary file
    BryanMon, 08-23-2021, created functions for UserInteraction class. Currently troubleshooting list appendage
    BryanMon, 08-23-2021, Troubleshooting Try/Except block for function update_game_count
    BryanMon, 08-24-2021, Fixed try/except for update_game_count
    BryanMon, 08-24-2021, Completed menu options and debugged returns from update_game_count function
    BryanMon, 08-24-2021, Tested and resolved issue with writing updated list_table to binary file
    BryanMon, 08-24-2021, Added comments and function docstring. Completed script
"""

# Board Game Inventory
# This program is designed to demonstrate the use of Try/Except error handling as well as Pickling in Python.
# The program will use a binary file to hold a list of data containing inventory of boardgames.
# The data types are: Game Names (STR) and Inventory Count (INT)

'''
# Create or add to the game list (gamelist.dat)

import pickle  # open library module Pickle

lst_games = []

while True:
    gamename = input("Enter name of game: \n")
    if gamename == "exit":  # allows exit out of data entry
        exit()
    elif gamename == "save":
        obj_pickle_out = open("GameList.dat", "ab")  # open file with write bytes rights
        pickle.dump(lst_games, obj_pickle_out)  # take our data from our list and dump to our binary file
        obj_pickle_out.close()  # close file
    else:
        dict_row = [gamename.lower()]
        lst_games.append(dict_row)
        continue
'''

# --- Defined variables

str_user_choice = ""  # user menu selection variable
str_game_name = ""  # the name of the game captured from user
lst_inventory_data = []  # list for holding our file data

# --- Load list data from datafile

import pickle  # open library module Pickle

obj_pickle_in = open("GameList.dat", "rb")  # open file with read bytes rights
lst_inventory_data = pickle.load(obj_pickle_in)
obj_pickle_in.close()  # close file


# --- Functions for Processing Data --- #
class DataProcess:

    # Display current list data
    @staticmethod
    def display_current_list(lst_data):
        """ Prints contents of list table

        :param lst_data: (list)
        :return: lst_data (list)
        """
        print("   Game Name   " + "   Inventory Count   ")  # list header
        print("-" * 40)  # format after header
        for lst_row in lst_data:  # loop through list_table and print row data
            print(lst_row)  # list the contents of dict_row
            print("-" * 40)  # format after each entry
        return lst_data

    # Append to data file
    @staticmethod
    def write_checkout_file(lst_data):
        """ Saves passed lst table to binary file via pickle

        :param lst_data: list
        :return: list
        """
        import pickle  # open library module Pickle

        obj_pickle_out = open("GameList.dat", "wb")  # open file with write bytes rights
        pickle.dump(lst_data, obj_pickle_out)  # take our data from our list and dump to our binary file
        obj_pickle_out.close()  # close file

        return lst_data


# --- Functions for I/O operations --- #
class UserInteraction:
    # Check for game on the list
    @staticmethod
    def check_game_exist(lst_check):
        """Receive user input and checks against entries from passed list table

        :param lst_check:
        :return: game_name (string) string of entered game name
        """
        game_name = input("Enter the name of the board game: \n")  # capture game name
        for row in lst_check:  # loop through our list_table
            if str(row[0]) == game_name.lower():  # search for a matching row
                print("Game found on list \n")
                return game_name  # if found, return to main menu
        else:
            print("\nThis game is not on the list of available games, please enter a valid entry \n")
            print("Returning to main menu. Select option 1 to view a valid list of games \n\n")
            game_name = None  # set game_name variable to none, pass the value back to main program
            return game_name

    # Update Inventory Count
    @staticmethod
    def update_game_count(game_name, lst_check):
        """Update game inventory count based on parsed game name and list table

        :param game_name: (string) name of game passed into function
        :param lst_check: (list)
        :return: game_name (string), lst_check (list) list table updated with new count
        """
        while True:
            try:  # Try block to verify legitimacy of user input for inventory count. Expect positive, whole integers
                int_game_count = int(input("\nEnter the updated count: \n"))
                if int_game_count < 0:  # if user input is less than zero
                    raise ValueError  # move to except block
                else:
                    for lst_row in lst_check:  # loop each row through our list
                        if lst_row[0] == game_name:  # check for list row equalling our game_name string
                            lst_check.remove(lst_row)  # remove the existing row matching our game_name
                            lst_row = [game_name, int_game_count]  # new row variable containing game name and inventory
                            lst_check.append(lst_row)  # append the new row to the lst_table
                            return game_name, lst_check  # exit function returning game_name (str) and lst table []
                continue
            except ValueError:  # raised if user input is less than zero, or non-integer
                print("\nPlease enter a whole number greater than zero\n")
                continue


# --- Presentation --- #

while True:
    print("""
    Menu of Options
    1) Show Current Game List
    2) Update Inventory Count
    3) Save Data to File
    4) Exit Program
    """)
    str_user_choice = input("Enter your selection [1 to 4]: \n")  # take menu selection input from user

    # -----------------------------------------------
    # 1) Show current game list
    if str_user_choice.strip() == '1':
        DataProcess.display_current_list(lst_inventory_data)
        continue  # return to main menu

    # -----------------------------------------------
    # 2) Update an items inventory count
    elif str_user_choice.strip() == '2':
        print("To update inventory count, please enter the following information: \n")
        str_game_name = UserInteraction.check_game_exist(lst_inventory_data)
        if str_game_name is None:  # if game is not found, loop back to main menu
            continue
        else:
            str_game_name, lst_inventory_data = UserInteraction.update_game_count(str_game_name, lst_inventory_data)
            continue  # return to main menu

    # -----------------------------------------------
    # 3) Save current list table to binary file
    elif str_user_choice.strip() == '3':
        print("\n\n\nSaving data to file... \n")
        DataProcess.write_checkout_file(lst_inventory_data)
        continue  # return to main menu

    # -----------------------------------------------
    # 4) Exit program
    elif str_user_choice.strip() == '4':  # Exit Program
        print("\n\nExiting Program\n\n")
        break  # Exit Program
