# Escribe un programa que encuentre el valor mínimo y máximo de una
# tupla de números.

def tuplas():
    tupla = (1, 2, 3, 4, 8, 4, 10)
    
    minimo = tupla[0]
    maximo = tupla[len(tupla) - 1]

    print(f'# Tupla base: {tupla}')

    for i in range(len(tupla)):
        if tupla[i] < minimo:
            minimo = tupla[i]
        
        elif tupla[i] > maximo:
            maximo = tupla[i]

    print(f'# Valor minimo de la tupla: {minimo}')
    print(f'# Valor maximo de la tupla: {maximo}')



if __name__ == '__main__':
    tuplas()