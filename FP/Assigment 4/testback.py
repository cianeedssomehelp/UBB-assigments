from assigment4 import consistent, solution, bkt_rec, bkt_iter, generate_subsequences

solutioncnt = 0

def test_consistent():
    assert consistent([0, 1]) == True
    assert consistent([0, -1]) == True
    assert consistent([0, 2]) == True
    assert consistent([0, -2]) == True
    assert consistent([0, 3]) == False
    assert consistent([1, -1]) == True
    print("All test cases for `consistent` passed")

def test_solution():
    assert solution([0, 1, 0], 1) == True
    assert solution([0, -1, 0], 1) == True
    assert solution([0, 1, -1, 0], 1) == False
    assert solution([0, 1, 2, 1, 0], 2) == True
    print("All test cases for `solution` passed")

def test_bkt_rec():
    global solutioncnt
    solutioncnt = 0
    bkt_rec([0], 1)
    assert solutioncnt > 0
    solutioncnt = 0
    bkt_rec([0], 2)
    assert solutioncnt > 0
    print("All test cases for `bkt_rec` passed")

def test_bkt_iter():
    global solutioncnt
    solutioncnt = 0
    bkt_iter([0], 1)
    assert solutioncnt > 0
    solutioncnt = 0
    bkt_iter([0], 2)
    assert solutioncnt > 0
    print("All test cases for `bkt_iter` passed")

def test_generate_subsequences():
    global solutioncnt
    solutioncnt = 0
    generate_subsequences(1)
    assert solutioncnt > 0
    solutioncnt = 0
    generate_subsequences(2)
    assert solutioncnt > 0
    print("All test cases for `generate_subsequences` passed")

def run_all_tests():
    test_consistent()
    test_solution()
    test_bkt_rec()
    test_bkt_iter()
    test_generate_subsequences()
    print("All tests passed!")