import copy
import pandas as pd

def __main__():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vigenere = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']]

    times = 0
    while times <= 24:
        alphabet.append(alphabet.pop(0))
        vigenere.append(list(alphabet))
        times += 1

    df = pd.DataFrame(vigenere, index=vigenere[0], columns=vigenere[0])
    df.index.name = 'id'
    df.to_csv('vigenere_table.csv')

__main__()