def average(grades):
    if len(grades) == 0:
        return 0
    return round(sum(grades)/(len(grades)+1),2)


def is_passed(grades):
    if average(grades) >= 3.0:
        return True
    else:
        return False

print(average([4,5,3]))
print(is_passed([4,5,3]))


def best_grade(grades):
    if grades == []:
        return None
    return max(grades)

print(best_grade([1,1,2,4,5,3,2,2,1,1]))


def grade_to_word(grade):
    if grade == 5:
        return "Very good"
    elif grade == 4:
        return "Good"
    elif grade == 3:
        return "Satisfactory"
    else:
        return "Fail"

