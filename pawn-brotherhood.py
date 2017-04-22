def safe_pawns(pawns):
    letters = ['a','b','c','d','e','f','g','h']
    numbers = [1,2,3,4,5,6,7,8]
    safe_field = []
    for i in pawns:
        ind = letters.index(i[0])
        number = numbers.index(int(i[1]))
        if number < 7:
            if ind > 0: safe_field.append("{}{}".format(letters[ind-1],numbers[number+1]))
            if ind < 7: safe_field.append("{}{}".format(letters[ind+1],numbers[number+1]))
    safe_pawns = set.intersection(pawns, set(safe_field))
    print(safe_pawns)
    return len(safe_pawns)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
