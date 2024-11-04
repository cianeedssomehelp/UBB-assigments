

"""
Recursive binary search is an algorithm that finds a number of your choosing from a sorted list dividing the list each time using its middle element.
If the number you are trying to find is less than the middle element, the algorithm continues looking for your number in the left part of the list and so on.
If the number you are trying to find is bigger than the middle element, the algorithm continues looking for your number in the right part of the list and so on.
"""


# Returns index of x in arr if present, else -1
def binarysearch(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == x:         # If element is present at the middle itself
            return mid

        elif arr[mid] > x:       # If element is smaller than mid, then it can only be present in left subarray
            return binarysearch(arr, low, mid-1, x)

        else:                           # Else the element can only be present in right subarray
            return binarysearch(arr, mid + 1, high, x)
    # Element is not present in the array
    else:
        return -1


"""
A binary test function that verifies if our binary search algorithm works well.
"""

def test_binarysearch():
    arr = [1, 2, 3, 4, 5]
    result_1 = binarysearch(arr, 0, len(arr) - 1, 3)  # Expected: 2
    assert binarysearch(arr, 0, len(arr) - 1, 3) == 2
    print(f"Test 1 - Searching 3: {result_1}")  # Found at index 2

    result_2 = binarysearch(arr, 0, len(arr) - 1, 1)  # Expected: 0
    print(f"Test 2 - Searching 1: {result_2}")  # Found at index 0

"""
Exchange sort is a sorting algorithm that sorts your list by comparing your i (0, n) 
element with your j (i+1, n) element and it goes on until all the elements are sorted.
There is also an implemented step algorithm that shows the progress of the sorting.
"""


def exchange_sort(num, step):
    size = len(num)
    swapcount = 0
    for i in range(size - 1):
        for j in range(i + 1, size):
            # Sorting into ascending order if previous element bigger than next element we swap to make it in ascending order
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
                swapcount += 1
            if swapcount % step == 0:
                print(f"Partially sorted list after {swapcount} steps:", num)


"""
A test function that verifies if our exchange sort algorithm works well.
"""

def test_exchange_sort():
    num = [5, 3, 4, 1, 2]
    print("Before exchange_sort:", num)
    exchange_sort(num, step=2)  # Step every 2 swaps
    print("After exchange_sort:", num)  # Check if sorted

"""
Strand sort is a recursive sorting algorithm that takes the first element (and the first remaining ones and so on) of the list, 
creates a sublist by finding each element bigger than this one and then uses a temporary list to store them.
It continues to create sub-lists in the same way and before it starts again, if there are two sub-lists it merges them by going through their elements and 
putting them in a list from the smallest one to the biggest one. 
There is also an implemented step algorithm that shows the progress of the sorting.
"""


def merge_lists(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result += list1
    result += list2
    return result

def strandsublist(ip, step, swapcount):
    if not ip:
        return []
    sublist = [ip.pop(0)] # Initialize a sublist with the first element of the input list
    i = 0
    while i < len(ip):
        # If the current element in the input list is greater than the last element in the sublist, add it to the sublist; otherwise, continue to the next element in the input list.
        if ip[i] > sublist[-1]:
            sublist.append(ip.pop(i))
            swapcount += 1
            if swapcount % step == 0:
                print(f"Partially sorted list after {swapcount} steps:", sublist)
        else:
            i += 1
    return sublist, swapcount

def strand_sort(ip, step):

    if len(ip) <= 1: # Base case: if the input list has 1 or fewer elements, it's already sorted
        return ip

    swapcount = 0
    sorted_list = []
    while ip:
        sublist, swapcount = strandsublist(ip, step, swapcount)
        sorted_list = merge_lists(sorted_list, sublist)
    return sorted_list

"""
A test function that verifies if our exchange sort algorithm works well.
"""

def test_strand_sort():
    num = [4, 2, 5, 1, 3]
    print("Before strand_sort:", num)
    sorted_num = strand_sort(num.copy(), step=2)  # Step every 2 operations
    print("After strand_sort:", sorted_num)  # Check if sorted