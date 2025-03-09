#
#   (E) - undo the list
#

def undo_length(history):
    return len(history)

def undo_operations(complex, history):
    if len(history) <= 1 :
        raise ValueError("Undo not available")

    previous_state = history.pop()
    complex.clear()
    complex.extend(previous_state)
    return complex, history
