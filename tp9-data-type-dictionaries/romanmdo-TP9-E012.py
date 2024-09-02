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

    diccionario_nuevo = {}

    print(f'# Nuevo diccionario: ')

    for i in estudiante_1:
        diccionario_nuevo[i] = [estudiante_1[i], estudiante_2[i]]
        print(f'- {i}: {diccionario_nuevo[i]}')

if __name__ == '__main__':
    diccionarios()