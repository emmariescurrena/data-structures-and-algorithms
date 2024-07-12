"""Random characters picker

Import passwords
"""
import random
from csv import writer
import csv

print('Bienvenido a PassGenarator')

CHARS_LIST = 'ABCDEFGHIJKLMNÑOPQRSTUVWYZabcdefghijklmnñopqrstuvwxyz1234567890!"#$%&/()=?¡¿*+.-'
output = []

print('¿Que quieres hacer?')
funcion = input ('0 Crear Contraseña | 1 Ver Contraseñas: ')
funcion = int(funcion)

if funcion == 0:
    site = input('Para que es la contraseña: ')
    user = input('Cual es el usuario: ')

    NUMBER = 1
    NUMBER = int(NUMBER)

    length = input ('Selecciona el largo de la contraseña: ')
    length = int(length)

    print('\nAqui tienes tus credenciales: ')

    for pwd in range(NUMBER):
        PASSWORDS = ''

        for c in range(length):
            PASSWORDS += random.choice(CHARS_LIST)
        output = [
            [site,user,PASSWORDS]
        ]
        def export ():
            """Export PASSWORDS"""
            with open('pass.csv', 'a', newline='', encoding='utf-8') as file:
                writer_object = writer(file)
                writer_object.writerow(output)
            file.close()
        export()
        print(output)
elif funcion == 1:
    def read ():
        """Read passwords"""
        with open('pass.csv', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                print(row)
    read()
else:
    print('Has introducido un valor incorrecto')
