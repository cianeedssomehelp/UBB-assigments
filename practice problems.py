
#first set

"""
2. Given natural number n, determine the prime numbers p1 and p2 such that n = p1 + p2 (check the Goldbach hypothesis).

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n // 2 + 1, 2):
            if n % i == 0:
                return False
    return True

def sum_prime(n: int):
    for p1 in range(2, n):
        if is_prime(p1):
            p2 = n - p1
            if is_prime(p2):
                return p1, p2

def main():
    line = int(input("Give the number n = "))
    if line <= 0:
        raise TypeError("N must be a natural number")
    elif line % 2 != 0:
        raise TypeError("N cannot be written as a sum of p1 and p2 prime numbers")
    else:
        print("The two prime numbers that summed up are our given number are", sum_prime(line))
main()
"""

"""
3. For a given natural number n find the minimal natural number m formed with the same digits. (e.g. n=3658, m=3568).


def digits(n: int): #Puts each digit of the number into a list
    dig = []
    while n > 0:
        dig.append(n % 10)
        n = n // 10
    return dig

def sort_list(dig_list): #Sorts the list in ascending order
    for i in range(len(dig_list)-1):
        for j in range(i+1, len(dig_list)):
            if dig_list[i] > dig_list[j]:
                aux = dig_list[i]
                dig_list[i] = dig_list[j]
                dig_list[j] = aux
    return dig_list

def minimal(dig_list): # Creates the minimal number out of the digits of the first number
    m=0
    for digit in dig_list:
        m = m * 10 + digit
    return m

def main():
    line = int(input("Give the number n = "))
    if line <= 0:
        raise TypeError("N must be a natural number")
    else:
        digits_list = digits(line)
        sort = sort_list(digits_list)
        if sort[0] == 0:
            for i in range(1,len(sort)): #if the list starts with a zero it makes sure the number doesnt start with a zero as well
                if sort[i] != 0:
                    a = sort[i]
                    sort[i] = sort[0]
                    sort[0] = a
                    break
    print("The minimal natural number m is ", minimal(digits_list))
main()

"""

"""
4. For a given natural number n find the largest natural number written with the same digits. (e.g. n=3658, m=8653).


def digits(n: int): #Puts each digit of the number into a list
    dig = []
    while n > 0:
        dig.append(n % 10)
        n = n // 10
    return dig

def sort_list(dig_list): #Sorts the list in descending order
    for i in range(len(dig_list)-1, 0, -1):
        for j in range(len(dig_list)-1, i, -1):
            if dig_list[i] < dig_list[j]:
                aux = dig_list[i]
                dig_list[i] = dig_list[j]
                dig_list[j] = aux
    return dig_list

def minimal(dig_list): # Creates the minimal number out of the digits of the first number
    m=0
    for digit in dig_list:
        m = m * 10 + digit
    return m

def main():
    line = int(input("Give the number n = "))
    if line <= 0:
        raise TypeError("N must be a natural number")
    else:
        digits_list = digits(line)
        sort = sort_list(digits_list)
    print("The minimal natural number m is ", minimal(digits_list))
main()

"""

"""
5. Generate the largest prime number smaller than a given natural number n. If such a number does not exist, a message should be displayed.


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n // 2 + 1, 2):
            if n % i == 0:
                return False
    return True
def main():
    n = int(input("Give the number = "))
    if n < 0:
        raise TypeError("N needs to be a positive number.") #Error that comes up each time we input a string or a real number that is not also a natural number.
    else:
        for j in range(int(n)-1, 1, -1):
            if is_prime(j):
                print(j)
                break
main()
"""





