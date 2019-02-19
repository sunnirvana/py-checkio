#!/usr/bin/env checkio --domain=py run cipher-map2

# https://py.checkio.org/mission/cipher-map2/

# 
# END_DESC

def trans_90(grille):
    new_grille = list()
    n = len(grille[0])
    for i in range(n):
        new_row = ''
        for j in reversed(range(n)):
            new_row += grille[j][i]
        new_grille.append(new_row)
    # print(grille, new_grille)
    return new_grille

def decrypt(cipher_grille, ciphered_password):
    length = len(cipher_grille[0])
    clear = ''
    for i in range(length):
        for j in range(length):
            if cipher_grille[i][j] == 'X':
                clear += ciphered_password[i][j]
    return clear

def recall_password(cipher_grille, ciphered_password):
    text = ''

    # 1st
    cipher_grille_0 = cipher_grille
    text += decrypt(cipher_grille_0, ciphered_password)

    # 2nd
    cipher_grille_90 = trans_90(cipher_grille)
    text += decrypt(cipher_grille_90, ciphered_password)

    # 3rd
    cipher_grille_180 = trans_90(cipher_grille_90)
    text += decrypt(cipher_grille_180, ciphered_password)

    # 4th
    cipher_grille_270 = trans_90(cipher_grille_180)
    text += decrypt(cipher_grille_270, ciphered_password)

    return text


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