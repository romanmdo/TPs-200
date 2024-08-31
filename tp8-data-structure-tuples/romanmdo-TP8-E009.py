# Escribe un programa que encuentre el valor mínimo y máximo de una
# tupla de números.

def tuplas():
    tupla = (1, 2, 3, 4, 2)
    
    minimo = min(tupla)
    maximo = max(tupla)
   
    print(f'# Tupla base: {tupla}')

    print(f'# Valor minimo de la tupla: {minimo}')
    print(f'# Valor maximo de la tupla: {maximo}')


if __name__ == '__main__':
    tuplas()