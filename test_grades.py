from grades import average, is_passed, best_grade

def test_average():
    assert average([4,5,3]) == 4.0

def test_average_empty():
    assert average([]) == 0

def test_is_passed():
    assert is_passed([4,3]) == True

def test_is_not_passed():
    assert is_passed([2,3,2]) == False

def test_best_grade():
    assert best_grade([2,3,5,1,2]) == 5

def test_empty_list():
    assert best_grade([]) is None