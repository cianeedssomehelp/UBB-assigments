"""
Generate the first prime number larger than a given natural number.
"""
"""
To generate the first prime number larger than a given natural number we firstly use a function that determines if a number is prime or not.
Next, we use a loop that stars with our number to which we add 1 and we verify every number until we find the first prime number.
When the first prime number greater than our given natural number is found, we print it and then use a break that stops our loop for looking for further numbers.
"""
from sys import maxsize

def is_prime(n: int) -> bool: #A function that verifies if a number is prime by finding if each number has any other divisors than number one or itself.
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n // 2 + 1, 2): #The numbers that are checked to be divisors go up until at least the square root of the number which we're checking if its prime.
            if n % i == 0:
                return False
    return True
def main():
    try:
        line = int(input("Give the number = "))
        if line < 0:
            raise TypeError("N needs to be a positive number.") #Error that comes up each time we input a string or a real number that is not also a natural number.
        else:
            for j in range(int(line)+1 , maxsize):#Veriffing if we can find a number greater than n that is prime and stopping the loop as soon as we find it and print it
                if is_prime(j):
                    print(j) #Prints the first prime number larger than our given number.
                    break
    except ValueError:
        print("Please enter a natural number.")
main()

