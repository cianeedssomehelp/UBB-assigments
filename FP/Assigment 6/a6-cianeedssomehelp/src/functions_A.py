from functions import *

#
#   (A) Add a number to the list
#

def add_new_complex(complex, real, imag, history):
    """
    Function that adds a new complex number to the list.
    :param complex: list of complex numbers
    :param real: real part
    :param imag: imaginary part
    :param history: history of the complex numbers
    :return: complex list after adding the new complex number
    """
    try:
        history = save_history(complex, history)
        if type(real) != int or type(imag) != int:
            raise TypeError("Real and Imag should be integers.")
        z = create_complex(real, imag)
        complex.append(z)
        return complex, history
    except ValueError as ve:
        print(ve)


def insert_complex(complex, real, imag, index, history):
    """
    Inserts a new complex number into the list on a specific index.
    :param complex: list of complex numbers
    :param real: real part
    :param imag: imaginary part
    :param index: index on which complex number is to be inserted
    :param history: history of the complex numbers
    :return: complex list after insertion
    """
    try:
        history = save_history(complex, history)
        if type(real) != int or type(imag) != int:
            raise TypeError("Real and Imag should be integers.")
        z = create_complex(real, imag)
        z = set_real(z, real)
        z = set_imag(z, imag)
        complex.insert(index, z)
        return complex, history
    except TypeError as te:
        print(te)
        return complex, history


