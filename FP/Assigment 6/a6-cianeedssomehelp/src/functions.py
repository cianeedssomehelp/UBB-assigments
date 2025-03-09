from random import randint
from math import sqrt
from pdoc import pdoc

#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#

def create_complex(real: int, imag: int):
    """
        Create a complex number
        :param real: real part
        :param imag: imaginary part
        :return: the created number
    """
    if real == "":
        raise ValueError("Real should not be empty")
    elif imag == "":
        raise ValueError("Imag should not be empty")
    elif type(real) != int or type(imag) != int:
        raise TypeError("Real and Imag should be integers.")
    return{"real": real, "imag": imag}

# -- setters --

def set_real(z: dict, real):
    z["real"] = real
    return z

def set_imag(z: dict, imag):
    z["imag"] = imag
    return z

# -- getters --

def get_real(z : dict) -> int:
    return z["real"]

def get_imaginary(z : dict) -> int:
    return z["imag"]

def to_string(z : dict):
    """
        Convert a complex number to string
        :param z: our complex number
        :return: the string representation of the complex number
    """
    real = get_real(z)
    imag = get_imaginary(z)
    if imag >= 0:
        sign = '+'
    else:
        sign = '-'

    if real == 0:
        return f"Complex number = {imag}i"
    elif imag == 0:
        return f"Complex number = {real}"
    elif imag == 0 and real == 0:
        return f"Complex number = 0"
    elif imag == 1:
        return f"Complex number = {real} {sign} i"
    else:
        return f"Complex number =  {real} {sign} {abs(imag)}i"

def readcomplex(complex: list, index: int):
    """
    Function that generates a list of complex numbers from the console.
    :param complex: our list of complex numbers in the form [real, imag]
    :param index: how many numbers in the list to generate
    :return: our list of complex numbers in the form [real, imag]
    """
    complex.clear()
    for i in range (0, index):
        real = int(randint(0, 30))
        imag = int(randint(0, 30))
        z = create_complex(real, imag)
        complex.append(z)
    return complex

def modulus(z):
    """
        Function that finds the modulus of a complex number.
        :param z: our list of complex numbers
        :return: the absolute value of the complex number
        """
    modul = sqrt(z["real"] ** 2 + z["imag"] ** 2)
    return modul

def save_history(complex, history):
    """
    Function that saves the history of the complex numbers list to it is easy to undo any operations.
    :param complex: list of complex numbers
    :param history: history of the complex numbers
    :return: history of the complex numbers
    """
    history.append(complex[:])
    return history


if __name__ == "__main__":
    """
    Generate HTML documentation using the pdoc package
    """
    f = open("doc.html", "wt")
    f.write(pdoc("functions.py"))
    f.write(pdoc("functions_A.py"))
    f.write(pdoc("functions_B.py"))
    f.write(pdoc("functions_D.py"))
    f.write(pdoc("functions_E.py"))
    f.close()
