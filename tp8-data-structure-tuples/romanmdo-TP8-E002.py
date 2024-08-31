# Crea un programa que tome una tupla de números y muestre el segundo y
# penúltimo elemento.

def tuplas():
    tupla = (1, 2, 3, 4, 5)
    caracter2do = tupla[1]
    caracterN = tupla[len(tupla) - 2]

    print(f'# Su tupla es: {tupla}')
    print(f'# Segundo caracter de la tupla: {caracter2do}')
    print(f'# Ultimo caracter de la tupla: {caracterN}')

if __name__ == '__main__':
    tuplas()