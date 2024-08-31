# Crea un programa que verifique si una clave
# específica existe en un diccionario de datos de contacto.

def diccionarios():
    diccionario = {
        'nombre' : 'mdo',
        'email' : 'mdo69@gmail.com',
        'numero' : 3584567869
    }

    print(f'# Elementos del diccionario: ')
    for i in diccionario:
        print(f'- {i}: {diccionario[i]}')



if __name__ == '__main__':
    diccionarios()