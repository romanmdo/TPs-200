# Crea un diccionario con información de un estudiante (nombre,
# grado, edad). Luego, permite al usuario actualizar la edad del estudiante.

def diccionarios():
    estudiante = {
        'nombre' : 'Mdo',
        'edad' : '20',
        'curso' : '2do año'
    }

    print(f'# Estudiante: ')
    for i in estudiante:
        print(f'- {i}: {estudiante[i]}')

    age = int(input('# Ingresa la edad del estudiante: '))
    estudiante['edad'] = age

    print(f'# La nueva edad del estudiante es: {estudiante["edad"]}')
    print(f'# Su nuevo diccionario es: {estudiante}')



if __name__ == '__main__':
    diccionarios()