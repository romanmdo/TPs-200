# Escribe un programa que solicite al usuario ingresar un
# string y luego imprima el primer y último carácter de ese string.

def cadenas():
    cadena = input(f'# Ingresa un string: ')

    caracter1 = cadena[0]
    caracterN = cadena[len(cadena) - 1]

    print(f'Primer caracter {caracter1}; Ultimo caracter {caracterN}')
    
if __name__ == '__main__':
    cadenas()