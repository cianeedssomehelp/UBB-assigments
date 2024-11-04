from sortandsearch import binarysearch, exchange_sort, strand_sort
from assigment3 import is_sorted, generateworstcasedata, generaterandomlist, generateaveragecasedata, generatebestcasedata, time_algorithm

# Test cases

def test_is_sorted():
    assert is_sorted([1, 2, 3, 4, 5]), "The list should be sorted."
    assert is_sorted([5, 5, 5]), "The list with equal elements should be sorted."
    assert not is_sorted([3, 1, 4, 2]), "The list should not be sorted."

def test_binarysearch():
    arr = [1, 2, 3, 4, 5]
    assert binarysearch(arr, 0, len(arr) - 1, 3) == 2, "Element 3 should be at index 2."
    assert binarysearch(arr, 0, len(arr) - 1, 6) == -1, "Element 6 should not be found."
    assert binarysearch(arr, 0, len(arr) - 1, 1) == 0, "Element 1 should be at index 0."

def test_exchange_sort():
    num = [5, 3, 4, 1, 2]
    exchange_sortwstep(num, step=2)
    assert num == [1, 2, 3, 4, 5], "The list should be sorted after exchange sort."

def test_strand_sort():
    num = [4, 2, 5, 1, 3]
    sorted_num = strand_sortwstep(num.copy(), step=2)
    assert sorted_num == [1, 2, 3, 4, 5], "The list should be sorted after strand sort."

def test_generate_random_list():
    random_list = generaterandomlist(10)
    assert len(random_list) == 10, "Length of the list should be 10."
    assert all(0 <= num <= 1000 for num in random_list), "All numbers should be between 0 and 1000."

def test_generate_worst_case_data():
    worst_case = generateworstcasedata(5)
    assert worst_case == [5, 4, 3, 2, 1], "Worst case should be in descending order."

def test_generate_average_case_data():
    average_case = generateaveragecasedata(5)
    assert len(average_case) == 5, "Length of list should be 5."
    assert all(0 <= num <= 1000 for num in average_case), "All numbers should be between 0 and 1000."

def test_generate_best_case_data():
    best_case = generatebestcasedata(5)
    assert best_case == [0, 1, 2, 3, 4], "Best case should be in ascending order."

def test_time_algorithm():
    random_list = generaterandomlist(10)
    time_taken = time_algorithm(exchange_sort, random_list.copy())
    assert time_taken >= 0, "Time taken should be non-negative."

# Run all tests
def run_tests():
    test_is_sorted()
    test_binarysearch()
    test_exchange_sort()
    test_strand_sort()
    test_generate_random_list()
    test_generate_worst_case_data()
    test_generate_average_case_data()
    test_generate_best_case_data()
    test_time_algorithm()
    print("All tests passed!")

# Trigger the test runner
run_tests()