import pandas as pd


ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def __main__():

    c_message = input('Enter message to decipher: ')
    key = input('Insert key: ')

    d_message = ''
    keyIndex = 0

    for i in range(len(c_message)):
        index = ALPHABET.index(c_message[i])-ALPHABET.index(key[keyIndex])
        if index < 0:
            index += 26
        d_message += ALPHABET[index]
        if keyIndex == 9:
            keyIndex = 0
        else:
            keyIndex += 1

    print(d_message)

    with open('decipher_messages.txt', 'w') as f:
        f.write(d_message)


__main__()
