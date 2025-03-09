from functions import *
#
#   (D) Filter the list
#

def filter_real(complex, value, history):
    """
    Function that filters a complex number in regard to imaginary part from the list.
    :param complex: list of complex numbers
    :param value: imaginary part of the complex number
    :param history: history of the complex numbers
    :return: filtered complex list
    """
    try:
        history = save_history(complex, history)
        filteredreal = []
        for z in complex:
            if z["imag"] == value:
                filteredreal.append(z)
        complex.clear()
        complex.extend(filteredreal)
        return complex, history
    except TypeError as te:
        print(te)
        return complex, history

def filter_modulo(complex, history, condition, value):
    """
    Function that filters complex numbers from the list in regard to its modulus.
    :param complex: list of complex numbers
    :param history: history of the complex numbers
    :param condition: condition to filter the complex numbers by
    :param value: value to filter the complex numbers by
    :return: filtered list of complex numbers
    """
    try:
        history = save_history(complex, history)
        filteredmodulus = []
        if condition == "<":
            for i in range(len(complex)):
                if modulus(complex[i]) < value:
                    filteredmodulus.append(complex[i])
        elif condition == ">":
            for i in range(len(complex)):
                if modulus(complex[i]) > value:
                    filteredmodulus.append(complex[i])
        elif condition == "=":
            for i in range(len(complex)):
                if modulus(complex[i]) == value:
                    filteredmodulus.append(complex[i])
        else:
            raise ValueError("Invalid condition")
        complex.clear()
        complex.extend(filteredmodulus)
        return complex, history
    except ValueError as ve:
        print(ve)
        return complex, history