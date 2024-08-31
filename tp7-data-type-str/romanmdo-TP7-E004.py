# Realiza un programa que repita una palabra ingresada por el
# usuario tres veces en una sola línea.

def cadenas():
    cadena1 = input(f'# Ingresa un string: ')
    repetir = cadena1 * 3

    print(f'{repetir}')
    
if __name__ == '__main__':
    cadenas()