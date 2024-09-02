# Crea dos diccionarios que representen la información de dos
# estudiantes diferentes. Combina ambos diccionarios en uno solo que contenga todos
# los datos.

def diccionarios():
    estudiante_1 = {
        'nombre' : 'mdo',
        'apellido' : 'maldonado',
    }

    estudiante_2 = {
        'nombre' : 'tto',
        'apellido' : 'miranda',
    }

    diccionario_nuevo = {
    }

    print(f'# Estudiantes: ')

    for i in estudiante_1:
        pass
    
    
    print(f'# Diccionario alumno 1: {estudiante_1}')
    print(f'# Diccionario alumno 2: {estudiante_2}')
    print(f'# Diccionario nuevo: {diccionario_nuevo}')

if __name__ == '__main__':
    diccionarios()