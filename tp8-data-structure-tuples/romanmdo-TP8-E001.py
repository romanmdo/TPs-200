# Escribe un programa que cree una tupla con los números del 1 al 5 y los
# imprima.

def tuplas():
    tupla = (1, 2, 3, 4, 5)
    for i in tupla:
        print(f'# Elemento: {i}')

if __name__ == '__main__':
    tuplas()