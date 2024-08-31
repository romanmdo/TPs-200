# Crea un programa que cuente cuántas veces aparece un número
# específico en una tupla

def tuplas():
    tupla = (1, 1, 2, 3, 4, 5)

    comprobacion = int(input('# Ingresa el numero para comprobar si se repite en la tupla: '))
    counter = 0

    for i in range(len(tupla)):
        if comprobacion == tupla[i]:
            counter += 1
    print(f'# El numero se repite {counter} veces')

if __name__ == '__main__':
    tuplas()