# Solve the problem from the third set here
"""
Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).
"""
"""
The program aims to find the largest perfect number that is smaller than a given number n. If such a number does not exist, a message should be displayed.
The program uses two separate functions. The 'perfect' function checks if the number we are analyzing is actually a perfect number by adding up its divisors, excluding itself.
The 'largest_perf_nr' is the function that checks if the perfect number is actually smaller than a given natural number n. If it isn't, a message is displayed that states so.
"""

def perfect(n: int) -> bool: #This is a function that checks if a number is perfect and returns True if it is, False if it is not.
    if n < 2:
        return False
    else:
        s = 1
        for i in range(2 , n):
            if n % i == 0:
                s = s + i
        if s == n:
            return True

def largest_perf_nr(n): #This function, with the help of our 'perfect' function, finds the largest perfect number that is smaller than a given natural number.
    for i in range(n-1 , 1, -1):
        if perfect(i):
            return i
    return "No perfect numbers smaller than n exist" #If there is no such perfect number, we print a message that states that fact.

def main():
    try:
        line = int(input("Give the number = "))
        if line < 0:
            raise TypeError("N needs to be a natural number") #Error that comes up each time we input a string or a real number that is not also a natural number.
        else:
            print(largest_perf_nr(line)) #Prints the largest perfect number that is smaller than our given natural number or just prints a message that states there is no such thing.
    except ValueError:
        print("N needs to be a natural number")
main()