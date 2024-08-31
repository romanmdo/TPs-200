# Escribe un programa que tome una tupla de cuatro elementos y desempaquete sus
# valores en cuatro variables, luego imprima esas variables.

def tuplas():
    tupla = (1, 2, 3, 4)
    a, b, c, d = tupla

    print(f'# Tupla base: {tupla}')
    print(f'# Elemento A de la tupla: {a}')
    print(f'# Elemento B de la tupla: {b}')
    print(f'# Elemento C de la tupla: {c}')
    print(f'# Elemento D de la tupla: {d}')


if __name__ == '__main__':
    tuplas()