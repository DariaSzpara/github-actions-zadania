import math

def average(grades):
    if len(grades) == 0:
        return 0
    return round(sum(grades) / len(grades), 2)


def is_passed(grades):
    if average(grades) >= 5.0:
        return True
    else:
        return False


def best_grade(grades):
    if grades == []:
        return None
    return max(grades)


def grade_to_word(grade):
    # Convert numeric grade to a word
    if grade == 5:
        return "very good"
    elif grade == 4:
        return "good"
    elif grade == 3:
        return "satisfactory"
    else:
        return "fail"


def has_one(grades):
    return 1 in grades
