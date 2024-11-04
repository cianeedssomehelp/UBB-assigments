"""
A menu-driven console application to help visualize the way searching and sorting algorithms work.
- Generate a list n of natural numbers. Generated numbers must be between 0 and 1000.
- Search for an item in the list using the algorithm you implemented.
- Sort the list using the first sorting algorithm.
- Sort the list using the second sorting algorithm.
- Exit the program.
"""

import random
from sortandsearch import binarysearch
from sortandsearch import exchange_sort
from sortandsearch import strand_sort
from sortandsearch import test_binarysearch
from sortandsearch import test_exchange_sort
from sortandsearch import test_strand_sort

"""
A function that creates a menu like interface from where the user can choose an option 
(the choices are implemented in the main function).
"""

def printMenu():
    print("1. Generate a list of n random natural numbers. Generated numbers must be between 0 and 1000.")
    print("2. Search for an item in the list using the algorithm you implemented.")
    print("3. Sort the list using a basic algorithm.")
    print("4. Sort the list using an advanced algorithm.")
    print("5. Print the list.")
    print("0. Exit the program.")

"""
A function that generates a random list with the numbers between 0 and 1000. 
Each time you want to start over with another list, the function clears the current list.
"""

def generaterandomlist(n, listofnumbers):
    listofnumbers.clear()
    for i in range(n):
        listofnumbers.append(random.randint(0, 1000))
    return listofnumbers

"""
Test function to see if the random list generator works just fine.
"""

def Testgeneraterandomlist():
    listofnumbers = []
    generated_list = generaterandomlist(5, listofnumbers)
    print("Generated random list:", generated_list)


"""
Print function.
"""

def printrandomlist(listofnumbers):
    print ("Here's your list! :D : ", listofnumbers)


"""
Function that checks if the list is already sorted before the program uses the implemented 
sorting algorithms.
"""

def is_sorted(listofnumbers):
    for i in range(len(listofnumbers)-1):
        if listofnumbers[i] > listofnumbers[i+1]:
            return False
    return True

"""
Test function to see if the is_sorted function works well.
"""

def test_is_sorted():
    list1 = [1, 2, 3, 4, 5]
    result1 = is_sorted(list1)
    print(f"Test case 1 - Is the list {list1} sorted? {result1}")

    list2 = [5, 5, 5, 5]
    result2 = is_sorted(list2)
    print(f"Test case 2 - Is the list {list2} sorted? {result2}")  # Expected: True

    # Test case 3: Unsorted list
    list3 = [3, 1, 4, 2]
    result3 = is_sorted(list3)
    print(f"Test case 3 - Is the list {list3} sorted? {result3}")  # Expected: False

"""
Main part of the program where all the choices for the menu items are implemented along with many
precautions that tell our program to stop at once if the input is not valid.
The first option helps you generate the random list and prints it so that you can see what you are working with.
The second option uses the binary search algorithm to search for a number of your choosing from the list. Don't forget the list must be sorted before choosing this option.
The third option lets you sort the list using exchange sort, a simple sorting algorithm that doesn't really have the best time and space complexity but it gets the job done.
The fourth option gives you the chance to sort the list using a more advanced sorting algorithm, strand sort.
For both of these algorithms there is included a step. You can choose to see progress of the sorting of the list by choosing a step (meaning the program will show you the progress each 1 sort or each 2 sorts).
"""


def main():
    listofnumbers = []

    Testgeneraterandomlist()
    test_binarysearch()
    test_is_sorted()
    test_exchange_sort()
    test_strand_sort()

    while True:
        printMenu()
        option = input("Which option would you like to choose? :D : ")
        if option == "0":
            print("Thank you!")
            break
        elif option == "1":
            try:
                n = int(input("Choose the size of the random list: "))
                generaterandomlist(n, listofnumbers)
                printrandomlist(listofnumbers)
            except ValueError:
                print("Please enter a natural number.")
        elif option == "2":
            if not listofnumbers:
                print("This list is empty. Generate a list first.")
            elif is_sorted(listofnumbers):
                try:
                    item_search = int(input("Choose an item to search from the list: "))
                    item_found = binarysearch(listofnumbers, 0, len(listofnumbers)-1, item_search)
                    if item_found != -1:
                        print("Item found at index: ", item_found)
                    else:
                        print("Item not found.")
                except ValueError:
                    print("Please enter a valid number to search for.")
            else:
                print("Please choose one of the sorting algorithms to sort the list first!")
        elif option == "3":
            if not listofnumbers:
                print("This list is empty. Generate a list first.")
            else:
                try:
                    step = int(input("Enter when you want to see a step of the sorting algorithm: "))
                    exchange_sort(listofnumbers, step)
                    printrandomlist(listofnumbers)
                except ValueError:
                    print("Please enter a natural number.")
        elif option == "4":
            if not listofnumbers:
                print("This list is empty. Generate a list first.")
            else:
                try:
                    step = int(input("Enter a step for strand sort: "))
                    listofnumbers = strand_sort(listofnumbers.copy(), step)
                    printrandomlist(listofnumbers)
                except ValueError:
                    print("Please enter a natural number.")
        elif option == "5":
            printrandomlist(listofnumbers)
        else:
            print("Invalid option. Please choose an option from 0-5 and try again.")
main()