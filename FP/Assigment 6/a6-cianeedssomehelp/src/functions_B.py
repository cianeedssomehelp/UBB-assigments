from functions import *
#
#   (B) Modify numbers
#

def remove_complex(complex: list, index: int, history: list, save_hist = True):
    """
    Function that removes a complex number from the list.
    :param complex: list of complex numbers
    :param index: index on which complex number is to be removed
    :param history: history of the complex numbers
    :param save_hist: bool type parameter that helps to not save history if it's not necessary (used with false value in a function below)
    :return: list of complex numbers after removing the complex number
    """
    if save_hist:
        history = save_history(complex, history)
    new_complex = []
    for i, c in enumerate(complex):
        if i != index:
            new_complex.append(c)
    complex = new_complex

    return complex, history

def remove_complex_in_range(complex, start, end, history):
    """
    Function that removes a range of complex numbers from the list.
    :param complex: list of complex numbers
    :param start: start index
    :param end: end index
    :param history: history of the complex numbers
    :return: the new complex list
    """
    history = save_history(complex, history)
    for i in range (end, start - 1, -1):
        complex, history = remove_complex(complex, i, history, save_hist = False)
    return complex, history

def replace_complex(complex, oldz, newz, history):
    history = save_history(complex, history)
    found = False
    for i in range(len(complex)):
        if complex[i] == oldz :
            complex[i] = newz
            found = True
    if not found:
        raise ValueError(f"Complex number {to_string(oldz)} not found in the list.")
    return complex, history
