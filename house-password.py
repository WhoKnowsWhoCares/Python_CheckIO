import re
def checkio(data):
    #replace this for solution
    if (len(data) >= 10) & \
            (re.search('[0-9]', data) is not None ) & \
            (re.search('[a-z]', data) is not None ) & \
            (re.search('[A-Z]', data) is not None ):
        return True

    # if len(data) < 10:
    #     return False
    #
    # containsNumber = False
    # containsLowLetter = False
    # containsUpperLetter = False
    #
    # for char in data:
    #     if not containsNumber:
    #         containsNumber = char.isnumeric()
    #     if not containsLowLetter:
    #         containsLowLetter = char.islower()
    #     if not containsUpperLetter:
    #         containsUpperLetter = char.isupper()
    # return containsNumber and containsLowLetter and containsUpperLetter

    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
