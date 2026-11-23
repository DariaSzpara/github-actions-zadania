def average(grades):
    if len(grades) == 0:
        return 0
    return round(sum(grades)/len(grades),2)


def is_passed(grades):
    if average(grades) >= 3.0:
        return True
    else:
        return False

print(average([4,5,3]))
print(is_passed([4,5,3]))