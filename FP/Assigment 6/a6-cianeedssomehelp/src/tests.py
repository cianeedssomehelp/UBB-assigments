
from functions_A import *
from functions_B import *
from functions_D import *
from functions_E import *

#
# The program's tests are implemented here.
#

def test_create_complex():
    z = create_complex(3, 4)
    assert z == {"real": 3, "imag": 4}, "test_create_complex failed"

    try:
        create_complex("", 4)
        assert False, "test_create_complex did not raise ValueError for empty real"
    except ValueError:
        pass

    try:
        create_complex(3, "")
        assert False, "test_create_complex did not raise ValueError for empty imag"
    except ValueError:
        pass


def test_modulus():
    z = {"real": 3, "imag": 4}
    assert modulus(z) == 5.0, "test_modulus failed"


def test_set_get():
    z = create_complex(3, 4)
    z = set_real(z, 5)
    assert get_real(z) == 5, "test_set_real or get_real failed"

    z = set_imag(z, 6)
    assert get_imaginary(z) == 6, "test_set_imag or get_imaginary failed"

def test_add_new_complex():
    complex_list = []
    history = []
    add_new_complex(complex_list, 3, 4, history)
    assert complex_list == [{"real": 3, "imag": 4}], "test_add_new_complex failed"
    assert len(history) == 1, "test_add_new_complex did not save history"


def test_insert_complex():
    complex_list = [{"real": 1, "imag": 1}]
    history = []
    insert_complex(complex_list, 3, 4, 0, history)
    assert complex_list == [{"real": 3, "imag": 4}, {"real": 1, "imag": 1}], "test_insert_complex failed"


def test_remove_complex():
    complex_list = [{"real": 3, "imag": 4}, {"real": 1, "imag": 1}]
    history = []
    complex_list, history = remove_complex(complex_list, 0, history)
    assert complex_list == [{"real": 1, "imag": 1}], "test_remove_complex failed"

def test_remove_complex_in_range():
    complex_list = [
        {"real": 1, "imag": 1},
        {"real": 2, "imag": 2},
        {"real": 3, "imag": 3}
    ]
    history = []
    complex_list, history = remove_complex_in_range(complex_list, 0, 1, history)
    assert complex_list == [{"real": 3, "imag": 3}], "test_remove_complex_in_range failed"

def test_replace_complex():
    complex_list = [{"real": 1, "imag": 1}, {"real": 2, "imag": 2}]
    history = []
    replace_complex(complex_list, {"real": 1, "imag": 1}, {"real": 3, "imag": 3}, history)
    assert complex_list == [{"real": 3, "imag": 3}, {"real": 2, "imag": 2}], "test_replace_complex failed"

def test_filter_real():
    complex_list = [
        {"real": 1, "imag": 0},
        {"real": 2, "imag": 2},
        {"real": 3, "imag": 0}
    ]
    history = []
    filter_real(complex_list, 0, history)
    assert complex_list == [{"real": 1, "imag": 0}, {"real": 3, "imag": 0}], "test_filter_real failed"

def test_filter_modulo():
    complex_list = [
        {"real": 3, "imag": 4},
        {"real": 1, "imag": 1}
    ]
    history = []
    filter_modulo(complex_list, history, ">", 2)
    assert complex_list == [{"real": 3, "imag": 4}], "test_filter_modulo failed"


def run_all_tests():
    test_create_complex()
    test_modulus()
    test_set_get()
    test_add_new_complex()
    test_insert_complex()
    test_remove_complex()
    test_remove_complex_in_range()
    test_replace_complex()
    test_filter_real()
    test_filter_modulo()
    print("All tests passed!")


if __name__ == "__main__":
    run_all_tests()
