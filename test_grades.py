
from grades import average, is_passed, best_grade, grade_to_word, has_one


def test_average():
    assert average([4, 5, 3]) == 4.0


def test_average_empty():
    assert average([]) == 0


def test_is_passed():
    assert is_passed([4, 3]) is True


def test_is_not_passed():
    assert is_passed([2, 3, 2]) is False


def test_best_grade():
    assert best_grade([2, 3, 5, 1, 2]) == 5


def test_empty_list():
    assert best_grade([]) is None


def test_grade_to_word():
    assert grade_to_word(5) == "very good"


def test_grade_to_word_fail():
    assert grade_to_word(2) == "fail"


def test_has_one_true():
    assert has_one([1, 2, 3]) is True


def test_has_one_false():
    assert has_one([2, 3, 4]) is False


def test_count_grades():
    assert count_grades([5, 4, 3]) == 3


def test_count_grades_empty():
    assert count_grades([]) == 0
