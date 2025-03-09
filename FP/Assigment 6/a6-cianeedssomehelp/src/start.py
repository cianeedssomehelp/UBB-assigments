from ui import *
from functions import *
#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#


def start():
    arr = []

    start_list_complex = [

        {"real": 6, "imag": 8},
        {"real": 3, "imag": 4},
        {"real": 13, "imag": 5},
        {"real": 0, "imag": 5},
        {"real": 3, "imag": 0},
        {"real": 3, "imag": 4},
        {"real": 6, "imag": 8},
        {"real": 0, "imag": 2},
        {"real": 5, "imag": 12},
        {"real": 7, "imag": 9}
    ]

    printList()
    choice = int(input("Please choose the list you would like to modify and such: "))
    if choice == 1:
        history = start_list_complex[:]
        complex = start_list_complex[:]
    elif choice == 2:
        complex = readcomplex(arr, 10)
        history = readcomplex(arr, 10)
    else:
        print("Invalid choice")
    print("Hi! Would you like to play with complex numbers?")
    get_input_from_user(complex, history)
if __name__ == "__main__":
    start()