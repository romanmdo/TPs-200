# Escribe un programa que tome un diccionario de países y
# capitales, y muestre todas las capitales.

def diccionarios():
    mapa_mundi = {
        'argentina' : 'Ciudad Autonoma de Bs As',
        'españa' : 'Madrid',
        'holmberg' : 'Casa Mdo'
    }

    print(f'# Capitales: ')
    for i in mapa_mundi:
        print(f'- Capital: {mapa_mundi[i]} ({i})')



if __name__ == '__main__':
    diccionarios()