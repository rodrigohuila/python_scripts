def palindromo(palabra):
    # Reemplazar espacios vacíos
    palabra = palabra.replace(' ', '')
    # Pasar la paalbra a minúsculas
    palabra = palabra.lower()
    # Variable almacenar la palabra invertida
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
# Dejar dos espacios es una buena práctica y standar


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


# Buena práctica en python
if __name__ == '__main__':
    run()
