import math
def checkio(a, b, c):
    angles = []
    if abs(a-b) >= c or abs(a+b) <= c: return [0,0,0]
    first = math.acos((a**2 + b**2 - c**2)/(2*a*b))/math.pi*180
    second = math.acos((a**2 + c**2 - b**2)/(2*a*c))/math.pi*180
    third = 180 - first - second
    print(first, second, third)
    #replace this for solution
    return sorted([round(first), round(second), round(third)], reverse=False)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
