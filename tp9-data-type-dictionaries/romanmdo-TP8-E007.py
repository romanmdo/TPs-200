# Escribe un programa que tome un diccionario de países y
# capitales, y muestre todas las capitales.

def diccionarios():
    diccionario = {
        'argentina' : 'Ciudad Autonoma de Bs As',
        'españa' : 'Madrid',
        'holmberg' : 'Casa Mdo'
    }

    print(f'# Elementos del diccionario: ')
    for i in diccionario:
        print(f'- Capital: {diccionario[i]} ({i})')



if __name__ == '__main__':
    diccionarios()