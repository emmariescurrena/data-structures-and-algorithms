
def __main__():

    word = input('Insert word to replace letters: ')

    while True:
        letter = []
        replacer = []
        temp = ''
        for l in word:
            if l == letter:
                l = replacer
            temp += l

        print(temp)


__main__()
