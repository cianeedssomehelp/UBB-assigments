"""
13. Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,... obtained from the sequence of natural numbers by replacing composed numbers with their prime divisors, without memorizing the elements of the sequence.
"""
#1,2,3,2,5,2,3,7,2,3,2,5,...

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

def sequenceprime(n):
    div_prim = []
    for i in range(2, n+1):
        if i == n:
            if i % 2 == 0:
                div_prim.append(2)
            for d in range(3, i // 2 + 1, 3):
                if n % d == 0:
                    div_prim.append(d)
    return div_prim




def main():
    n = int(input("Enter a number: "))
    if n <= 0:
        raise ValueError("Number must be greater than 0")
    else:
        print(sequence(n))
main()