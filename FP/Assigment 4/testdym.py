
from assigment5 import dynamicapproach, naiveapproach

def test_dynamicapproach():
    # Test case 1
    arr = [30, 5, 15, 18, 30, 40]
    length = len(arr)
    expected_value = 32
    expected_expression = "40 - 18 + 15 - 5"

    result_value, result_expression = dynamicapproach(arr, length)
    assert result_value == expected_value, f"Expected {expected_value}, got {result_value}"
    assert result_expression == expected_expression, f"Expected {expected_expression}, got {result_expression}"
    print("Test case 1 for dynamicapproach passed.")

    # Test case 2 (edge case with all negative numbers)
    arr = [-1, -2, -3, -4, -5]
    length = len(arr)
    expected_value = -2
    expected_expression = "(-5) - (-4) + (-3) - (-2)"

    result_value, result_expression = dynamicapproach(arr, length)
    assert result_value == expected_value, f"Expected {expected_value}, got {result_value}"
    assert result_expression == expected_expression, f"Expected {expected_expression}, got {result_expression}"
    print("Test case 2 for dynamicapproach passed.")

    # Additional test cases can be added as needed


def test_naiveapproach():
    # Test case 1
    arr = [30, 5, 15, 18, 30, 40]
    length = len(arr)
    expected_value = 32
    expected_expression = (40, 18, 15, 5)

    result_value, result_expression = naiveapproach(arr, length)
    assert result_value == expected_value, f"Expected {expected_value}, got {result_value}"
    assert result_expression == expected_expression, f"Expected {expected_expression}, got {result_expression}"
    print("Test case 1 for naiveapproach passed.")

    # Test case 2 (edge case with all negative numbers)
    arr = [-1, -2, -3, -4, -5]
    length = len(arr)
    expected_value = -2
    expected_expression = (-5, -4, -3, -2)

    result_value, result_expression = naiveapproach(arr, length)
    assert result_value == expected_value, f"Expected {expected_value}, got {result_value}"
    assert result_expression == expected_expression, f"Expected {expected_expression}, got {result_expression}"
    print("Test case 2 for naiveapproach passed.")

def run_tests():
    test_dynamicapproach()
    test_naiveapproach()
run_tests()

