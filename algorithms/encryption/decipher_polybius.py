TABLE = [[' ', ' ', ' ', ' ', ' ', ' '],
         [' ', 'a', 'b', 'c', 'd', 'e'],
         [' ', 'f', 'g', 'h', 'i', 'j'],
         [' ', 'k', 'l', 'm', 'n', 'o'],
         [' ', 'p', 'q', 'r', 's', 't'],
         [' ', 'u', 'v', 'w', 'x', 'y']]


def __main__():

    cMessage = input('Insert message to decipher: ')

    fMessage = ''
    first, second = 0, 1
    while second < len(cMessage):
        letter = TABLE[int(cMessage[second])][int(cMessage[first])]
        print(letter)
        first += 2
        second += 2
        fMessage += letter

    print(fMessage)
    with open('decipher_messages.txt', 'w') as f:
        f.write(fMessage)


__main__()
