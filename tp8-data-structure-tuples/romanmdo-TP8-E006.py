# Crea un programa que verifique si un número dado está presente en una
# tupla.

def tuplas():
    tupla = (1, 2, 3, 4)

    validacion = int(input(f'> Ingresa un valor para comprobar si esta en la tupla: '))
    
    for i in range(len(tupla)):
        if validacion == tupla[i]:
            print(f'# El valor {tupla[i]} esta en la tupla! ')
            break
        else:
            print(f'# El valor {tupla[i]} no esta en la tuplas')

    print(f'# Tupla base: {tupla}')

if __name__ == '__main__':
    tuplas()