def getMask(cipher_grille):
    result = []
    for i in range(len(cipher_grille)):
        result += [(i,ind) for ind, letter in enumerate(cipher_grille[i]) if letter == 'X']
    return result

def rotate(cipher_grille):
    result = ['','','','']
    for i in range(len(cipher_grille)):
        for j in range(len(result)):
            result[j] += cipher_grille[len(cipher_grille)-i-1][j]
    return result
    
def recall_password(cipher_grille, ciphered_password):
    line = ''
    new_pass = cipher_grille
    for i in range(4):
        print(new_pass)
        mask = getMask(new_pass)
        print(mask)
        line += ''.join([ciphered_password[x[0]][x[1]] for x in mask])
        print(line)
        new_pass = rotate(new_pass)
        
    return line

#def recall_password(cipher_grille, ciphered_password):
#    f1 = [list(word) for word in cipher_grille]
#    f2 = [list(word) for word in ciphered_password]  
#    stt = ""
#    tt = 0
#    while tt < 4:
#        for row in range(4):
#            for col in range(4):
#                if f1[row][col] == 'X':
#                    stt = stt + f2[row][col]    
#        ord1 = []
#        for row in range(4):
#            temp = []
#            for col in reversed(range(4)):
#        #        print(str(f1[col][row])+ " ",end="")
#                temp.append(f1[col][row])
#            ord1.append(temp)
#        f1 = ord1
#        tt += 1
#    return stt


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
