"""
Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2, larger than the given natural number n. (e.g. for n = 6, m = 8).
"""
"""
This program uses a function that returns the smallest fibonacci number lager than a given natural number.
We input our number. If it's not a natural number the program raises an error. If the number is natural, we go ahead and print the smallest fibonacci number larger than the input 
number that our function has found.
"""

def fibonacci_number(line): #A function that finds the smallest fibonacci number that is larger than a natural number n because our while loop stops when b is greater than "line"
    a = 1
    b = 1
    while b <= line:
        a = b
        b = a + b
    return b
def main():
    try:
        line = int(input("Give a natural number n = "))
        if line < 0:
            raise TypeError("N needs to be a natural number") #Error that comes up each time we input a string or a real number that is not also a natural number.
        else:
            m = fibonacci_number(line)
            print("The smallest Fibonacci number larger than n is", m) #Prints the smallest fibonacci number greater than our given natural number that our function has found.
    except ValueError:
        print("Please enter a natural number")
main()