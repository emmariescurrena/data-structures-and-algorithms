import time
import random


nombre = input("Bienvenido. Ingresar nombre: ")
print(f"Hola, {nombre}. Es hora de jugar al 'Forma la palabra'\n")
time.sleep(1)

palabra = (random.choice(open("diccionario.txt", "r").readlines())
           ).replace("\n", "")
palabra = "camión"
palabra = palabra.replace("á", "a").replace("é", "e").replace(
    "í", "i").replace("ó", "o").replace("ú", "u")
tupalabra = ''
intentos = 5

letras_probadas = []
caracteres = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
              "d", "f", "g", "h", "j", "k", "l", "ñ", "z", "x", "c", "v", "b", "n", "m"]

while intentos > 0:
    fallas = 0
    print(len(palabra), end=" ")
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end="")
        else:
            print("•", end="")
            fallas += 1
    if fallas == 0:
        print(
            f". Felicidades, {nombre}. Pudiste formar la palabra {palabra} (=")
        break
    else:
        tuletra = input("\nIntroducir una letra: ")[:1]
        tupalabra += tuletra
        letra_valida = False
        for caracter in caracteres:
            if caracter == tuletra:
                letra_valida = True
        if letra_valida == False:
            print(
                f"\nCaracter inválido. Te quedan {intentos} intentos.\nLetras probadas: {letras_probadas}")
        elif tuletra in letras_probadas:
            print(
                f"\nLetra ya probada. Te quedan {intentos} intentos.\nLetras probadas: {letras_probadas}")
        elif tuletra in palabra:
            letras_probadas.append(tuletra)
            print(
                f"\nCorrecta. Te quedan {intentos} intentos.\nLetras probadas: {letras_probadas}")
        else:
            letras_probadas.append(tuletra)
            intentos -= 1
            if intentos == 0:
                print(
                    f"\nLo siento, {nombre}. Te quedaste sin intentos. La palabra era {palabra}")
            else:
                print(
                    f"\nIncorrecta. Te quedan {intentos} intentos.\nLetras probadas: {letras_probadas}")
