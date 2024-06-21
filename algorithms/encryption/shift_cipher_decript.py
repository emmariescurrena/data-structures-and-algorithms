
ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def __main__():
    '''Translate text cipher to words'''

    c_message = input('Enter message to decipher: ')

    shift = 1
    all_messages = []
    while shift <= 25:
    
        d_message = []

        for l in c_message:
            d_message.append(ALPHABET.index(l))

        for i,n in enumerate(d_message):
            n += shift
            if n > 25:
                n -= 26
            d_message[i] = ALPHABET[n]
    
        f_message = ''
        for l in d_message:
            f_message += l

        all_messages.append(f_message)

        shift += 1

    with open('decipher_messages.txt', 'w') as f:
        for m in all_messages:
            f.write(f'{m}\n')

__main__()
