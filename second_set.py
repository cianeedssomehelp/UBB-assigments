"""
6. Determine a calendar date (as year, month, day) starting from two integer numbers representing the year and the day number inside that year (e.g. day number 32 is February 1st). Take into account leap years. Do not use Python's inbuilt date/time functions.


def isleapyear(year) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def getdateofyear(year, dayofyear):
    days_in_month_common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #last day of month in a common year
    days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #last day of month in a leap year
    if isleapyear(year):
        days_in_month = days_in_month_leap #if its a leap year sets the last days of the month to a last last days in leap year
    else:
        days_in_month = days_in_month_common
    month = 1  #starts from first month
    for days_in_current_month in days_in_month: #goes through each last day of the month through the months
        if dayofyear > days_in_current_month: #veriffies if the day we entered is not actually a calendar date
            dayofyear -= days_in_current_month #resets the day
            month += 1 #goes to the next month
        else:
            day = dayofyear #resets the day
            break
    return year, month, day


def main():
    day = int(input("Give the day = "))
    year = int(input("Give the year = "))
    if day <= 0 and year <= 0:
        raise TypeError("What we input must be natural numbers")
    else:
        print("The date is ", getdateofyear(year, day))
main()

"""

"""
7. Determine the twin prime numbers p1 and p2 immediately larger than the given non-null natural number n. Two prime numbers p and q are called twin if q - p = 2.


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

def twin_prime(n: int):
    for p1 in range(n+1, maxsize):
        if is_prime(p1):
            p2 = p1-2
            if is_prime(p2) and p2 != n:
                return p1, p2

def main():
    line = int(input("Give the number n = "))
    if line <= 0:
        raise TypeError("N must be a natural number")
    else:
        print("The two prime numbers that are twin numbers larger than our given number", twin_prime(line))
main()

"""

"""
9. Consider a given natural number n. Determine the product p of all the proper factors of n.


def product_proper(n: int):
    product = 1
    for i in range(2, n):
        if n % i == 0:
            product *= i
    return product

def main():
    n = int(input("Give the number n = "))
    if n <= 0:
        raise TypeError("N must be a natural number")
    else:
        print("The product of the proper divisors of n is ", product_proper(n))
main()

"""

"""
10. The palindrome of a number is the number obtained by reversing the order of its digits (e.g. the palindrome of 237 is 732). For a given natural number n, determine its palindrome.


def inverse(n):
    pal = 0
    while n > 0:
        pal = pal * 10 + n % 10
        n = n // 10
    return pal

def is_palindrome(n) -> bool:
    if inverse(n) == n:
        return True
    else:
        return False

def main():
    n = int(input("Give the number n = "))
    if n <= 0:
        raise TypeError("N must be a natural number")
    elif is_palindrome(n):
            print("The number is palindrome")
    else:
        print("The inverse of the number n is ", inverse(n))
main()
"""

"""
11. The numbers n1 and n2 have the property P if their writing in base 10 uses the same digits (e.g. 2113 and 323121). Determine whether two given natural numbers have property P.


def digits(n):
    digit_count = [0] * 10 #vector caracteristic
    while n > 0:
        digit = n % 10
        digit_count[digit] = 1 #de fiecare data cand verifica o cifra pune 1 daca cifra nu apare si ramane la fel daca cifra a mai aparut
        n = n // 10
    return digit_count

def haspropertyP(n1, n2) -> bool:
    freqn1 = digits(n1)
    freqn2 = digits(n2)
    if freqn1 == freqn2: #daca frecventele/vect caracteristici au aceleasi elemente in aceleasi locuri e true
        return True
    else:
        return False
def main():
    n1 = int(input("Give the number n1 = "))
    n2 = int(input("Give the number n2 = "))
    if n1 <= 0 and n2 <= 0:
        raise TypeError("N must be a natural number")
    else:
        if haspropertyP(n1, n2) == True:
            print("N1 and N2 have the property P ")
        else:
            print("N1 and N2 do not have the property P ")
main()

"""