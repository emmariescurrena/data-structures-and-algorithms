
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def __main__():
    '''Translate text cipher to words'''

    c_message = input('Enter message to decipher: ')

    f_message = ''
    for l in c_message:
        value = (ALPHABET.index(l)+1)*2-1
        if value > 25:
            value -= 26
        f_message += ALPHABET[value]

    with open('decipher_messages.txt', 'w') as f:
        f.write(f_message)


__main__()
