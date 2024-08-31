# Crea un diccionario con información de un estudiante (nombre,
# grado, edad). Luego, permite al usuario actualizar la edad del estudiante.

def diccionarios():
    diccionario = {
        'nombre' : 'Mdo',
        'edad' : '20',
        'curso' : '2do año'
    }

    age = int(input('# Ingresa la edad del estudiante: '))
    diccionario['Edad'] = age

    print(f'La nueva edad del estudiante es: {diccionario["Edad"]}')



if __name__ == '__main__':
    diccionarios()