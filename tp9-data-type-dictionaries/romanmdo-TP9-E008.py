# Crea un programa que verifique si una clave
# específica existe en un diccionario de datos de contacto.

def diccionarios():
    datos = {
        'nombre' : 'mdo',
        'email' : 'mdo69@gmail.com',
        'numero' : 3584567869
    }

    opcion = input(f'# Ingresa una clave para comprobar si existe: ')

    if opcion in datos:
        print(f'# Esta clave si existe en el diccionario! ')

    else: 
        print(f'# Esta clave no existe en el diccionario! ')

if __name__ == '__main__':
    diccionarios()