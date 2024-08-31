# Crea un programa que pida al usuario ingresar una palabra y luego
# muestre cuántos caracteres tiene esa palabra.

def cadenas():
    cadena = input(f'# Ingresa un string para ver su longitud: ')

    caracterLen = len(cadena)

    print(f'# El tamaño de su cadena de caracteres es de: {caracterLen}')
    
if __name__ == '__main__':
    cadenas()