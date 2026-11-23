from grades import average, is_passed

def test_average():
    assert average([4,5,3]) == 4.0

def test_average_empty():
    assert average([]) == 0

def test_is_passed():
    assert is_passed([4,3]) == True

def test_is_not_passed():
    assert is_passed([2,3,2]) == False