from functions import *
from functions_A import *
from functions_B import *
from functions_D import *
from functions_E import *
from texttable import Texttable
from math import sqrt
#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#

def printList():
    print("Which list would you like to play with?")
    print("1. The start up list.")
    print("2. The randomly generated list.")

def printMenu():
    print("Here are your options: ")
    print("1. Add or insert a number to the list.")
    print("2. Remove a number from the list or a range of numbers.")
    print("3. Replace a number.")
    print("4. Display the list.")
    print("5. Display numbers on criteria. You have to filter the list first!")
    print("6. Filter the list.")
    print("7. Undo.")
    print("0. Exit the application.")

def get_input_from_user(complex, history):

    while True:
        printMenu()
        try:
            choice = int(input("What would you like to do with your list? "))
            if choice < 0:
                raise ValueError("Error! That seems to be a negative number. Please try again.")
            if choice > 8:
                raise ValueError("Error! That seems to be an invalid number. Please try again.")
            if choice == 0:
                break
            elif choice == 1:
                print("Would you like to add or insert a number? ")
                condition = input("Type 'add' or 'insert': ").strip().lower()
                condition_dict = {"add": add_number_ui, "insert": insert_number_ui}
                if condition in condition_dict:
                    try:
                        complex, history = condition_dict[condition](complex, history)
                    except ValueError as ve:
                        print(ve)
                else:
                    print("Invalid choice. Please type 'add' or 'insert'.")
            elif choice == 2:
                print("Would you like to remove a number or remove multiple numbers? ")
                condition = input("Type 'rnum' or 'rrange': ").strip().lower()
                condition_dict = {"rnum": remove_number_ui, "rrange": remove_range_ui}
                if condition in condition_dict:
                    try:
                        complex, history = condition_dict[condition](complex, history)
                    except ValueError as ve:
                        print(ve)
                else:
                    print("Invalid choice. Please type 'rnum' or 'rrange'.")
            elif choice == 3:
                complex, history = replace_number_ui(complex, history)
            elif choice == 4:
                print("How would you like to display the list?")
                try:
                    display = int(input("Enter the option for the way you would like to display your list: "))
                    if type(display) != int:
                        raise ValueError("Error! That seems to not be an integer. Please try again.")
                    if display == 1:
                        displayList(complex)
                    elif display == 2:
                        displayTexttable(complex)
                except ValueError as ve:
                    print(ve)
            elif choice == 5:
                print("Would you like to display the filtered real list or the filtered modulo list? ")
                condition = input("Type 'realp' or 'modulo': ").strip().lower()
                condition_dict = {"realp": displayTableReal, "modulo": displayTableModulus}
                if condition in condition_dict:
                    try:
                        condition_dict[condition](complex)
                    except ValueError as ve:
                        print(ve)
                else:
                    print("Invalid choice. Please type 'realp' or 'modulo'.")
            elif choice == 6:
                print("Would you like to filter the list with the real or modulo condition?")
                condition = input("Type 'realf' or 'modulof': ").strip().lower()
                condition_dict = {"realf": filter_real_ui, "modulof": filter_modulo_ui}
                if condition in condition_dict:
                    try:
                        condition_dict[condition](complex, history)
                    except ValueError as ve:
                        print(ve)
                else:
                    print("Invalid choice. Please type 'realf' or 'modulof'.")
            elif choice == 7:
                complex, history = undo_operations(complex, history)
            else:
                print("Invalid choice. Please enter a valid number from 0 to 7.")
        except ValueError as ve:
            print(ve)

def add_number_ui(complex, history):
    try:
        real = int(input("real part = "))
        imag = int(input("imaginary part = "))
    except ValueError:
        raise ValueError("Real and Imaginary parts must be integers.")
    complex, history = add_new_complex(complex, real, imag, history)
    return complex, history

def insert_number_ui(complex, history):
    try:
        index = int(input("Enter the index you would like to insert your number on (any number from 0 - 10 or depends on the current list length: "))
        if index > len(complex):
            raise ValueError("Index out of range.")
        real = int(input("real part = "))
        imag = int(input("imaginary part = "))
    except ValueError:
        raise ValueError("Real and Imaginary parts must be integers. The index must also be an integer within the valid range.")
    complex, history = insert_complex(complex, real, imag, index, history)
    return complex, history

def remove_number_ui(complex, history):
    try:
        index = int(input("Select the index you would like to remove your number from: "))
    except ValueError:
        raise ValueError("Real and Imaginary parts must be integers.")
    complex, history = remove_complex(complex, index, history)
    return complex, history

def remove_range_ui(complex, history):
    try:
        start = int(input("Enter the index you would like to start removing your number from: "))
        end = int(input("Enter the index you would like to stop removing your number at: "))

        if start < 0 or end >= len(complex) or start > end:
            raise ValueError("Invalid range. Ensure you enter a valid range between 0 and the length of your array and that the indexes you introduced are integers.")

        history = save_history(complex, history)

        complex, history = remove_complex_in_range(complex, start, end, history)
        return complex, history
    except ValueError as e:
        print(e)
        return(complex, history)

def replace_number_ui(complex, history):
    try:
        oldreal = int(input("old real part = "))
        oldimag = int(input("old imaginary part = "))
        oldz = create_complex(oldreal, oldimag)

        newreal = int(input("new real part = "))
        newimag = int(input("new imaginary part = "))
        newz = create_complex(newreal, newimag)

        complex = replace_complex(complex, oldz, newz, history)
        history = replace_complex(complex, oldz, newz, history)
    except ValueError:
        raise ValueError("All real and imaginary parts entered must be integers.")
    return complex, history

def filter_real_ui(complex, history):
    try:
        value = int(input("Enter a value for the imaginary part to filter the list by: "))
        complex, history = filter_real(complex, value, history)
        return complex, history
    except ValueError:
        raise ValueError("All real and imaginary parts must be integers.")

def filter_modulo_ui(complex, history):
    try:
        condition = input("Enter the condition you want to filter the list by ( < or = or >): ")
        if condition not in ('<', '=', '>'):
            raise ValueError("Invalid condition. Please type '<', '=' or '>'.")
        value = int(input("Enter a value to filter the list by: "))
        if type(value) != int:
            raise ValueError("The value you entered is not an integer.")
        complex, history = filter_modulo(complex, history, condition, value)
        return complex, history
    except ValueError as ve:
        print(ve)

#
#   (C) Display numbers having different properties
#

def displayList(complex : list):
    for i in range(len(complex)):
        if isinstance(complex[i], dict):
            print(to_string(complex[i]))
        else:
            print(f"Invalid complex number format at index {i}: {complex[i]}")

def displayTexttable(complex: list):
    table = Texttable()
    table.add_row(['Complex', 'Real', 'Imaginary'])

    if complex:
        for i, num in enumerate(complex, start = 1):
            if not isinstance(num, dict):
                raise ValueError("Invalid complex number format at index {i}: {complex[i]}.")
            else:
                real = num["real"]
                imag = num["imag"]
                table.add_row([f"Complex {i}", real, imag])
        print("List of complex numbers: ")
        print(table.draw())
    else:
        print("No complex numbers found.")

def displayTableReal(complex):
    table = Texttable()
    table.add_row(['Complex', 'Real'])

    if complex:
        for i, num in enumerate(complex, start = 1):
            if not isinstance(num, dict):
                raise ValueError("Invalid complex number format at index {i}: {complex[i]}.")
            else:
                real = num["real"]
                table.add_row([f"Complex {i}", real])
        print("Filtered Real Numbers:")
        print(table.draw())  # Draw the table
    else:
        print("No purely complex numbers found with imaginary part = given value.")


def displayTableModulus(complex):
    table = Texttable()
    table.add_row(['Complex', 'Real', 'Imaginary', 'Modulus'])
    if not complex:
        return
    try:
        for i, num in enumerate(complex, start = 0):
            if not isinstance(num, dict):
                raise ValueError(f"Invalid complex number format at index {i}: {complex[i]}")
            else:
                real = num["real"]
                imag = num["imag"]
                modulo = sqrt((real ** 2) + (imag ** 2))
                table.add_row([f"Complex {i + 1}", real, imag, modulo])
        print("Filtered Complex Numbers by Modulus:")
        print(table.draw())
    except ValueError as ve:
        print(ve)