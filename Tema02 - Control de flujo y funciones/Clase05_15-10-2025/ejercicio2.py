# Elaborar una función que lea un caracter
# e indique si es una vocal o no.
# Ej1: A => Es una vocal
# Ej2: 4 => No es una vocal

def validarVocal(char):
    char = char.lower()
    vocales = ['a','e','i','o','u']
    esVocal = char in vocales
    # Empleamos la expresión ternaria
    return 'Es vocal' if esVocal else 'No es una vocal'

char = input('Ingresa el caracter: ')
print(validarVocal(char))