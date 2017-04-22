import math
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    degree = 0
    for i in range(1, len(powers)):
        if int(number/base**i) == 0: 
            degree = i - 1
            break
    if decimals != 0:
        result = "{0}{1}{2}".format(round(number/(base**degree)*(10**decimals)),powers[degree],suffix)
    else:
        result = "{}{}{}".format(int(number/base**degree),powers[degree],suffix)
    print(result)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

