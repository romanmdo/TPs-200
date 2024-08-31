# Escribe un programa que tome dos strings como entrada y
# los concatene en uno solo.

def cadenas():
    cadena1 = input(f'# Ingresa un string (este va a ser el string 1): ')
    cadena2 = input(f'# Ingresa un string (este va a ser el string 2): ')

    print(f'{cadena1} {cadena2}')
    
if __name__ == '__main__':
    cadenas()