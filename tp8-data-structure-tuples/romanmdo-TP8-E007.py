#  Escribe un programa que cree una tupla que contenga otras dos tuplas dentro de ella y
# luego imprima los elementos de las tuplas anidadas.

def tuplas():
    t1 = (1, 2, 3, 4, 5)
    t2 = (6, 7, 8, 9, 10)

    tuplas = (t1, t2)

    print(f'# Tupla anidada: {tuplas}')


if __name__ == '__main__':
    tuplas()