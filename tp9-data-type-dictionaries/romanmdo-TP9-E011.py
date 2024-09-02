# Escribe un programa que tome un diccionario y cree uno
# nuevo donde las claves sean los valores y los valores sean las claves del original.

def diccionarios():
    diccionario = {
        'condesa' : 500,
        'morgan' : 800,
        'roca' : 400
    }

    diccionario_nuevo = {
    }

    print(f'# Entradas para el rey de la noche: ')

    for i in diccionario:
        diccionario_nuevo[diccionario[i]] = i
    
    print(f'# Diccionario antiguo: {diccionario}')
    print(f'# Diccionario nuevo: {diccionario_nuevo}')

if __name__ == '__main__':
    diccionarios()