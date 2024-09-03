# Crea un diccionario que contenga información de varios
# empleados (nombre, cargo, salario). Luego, permite al usuario buscar un empleado
# por nombre y mostrar su información completa.

def diccionarios():
    empleados = {
        'jedi' : {
            'nombre' : 'hilario',
            'rol' : 'backend'
        },
        
        'mdo' : {
            'nombre' : 'roman',
            'rol' : 'frontend'
        },
    }

    opcion = input(f'# Ingresa un empleado para buscaralo: ')

    for i in empleados:
        if opcion == i:
            print(f'# Empleado encontrado: ')
            print(f'# Empleado: {i} --> {empleados[i]}')
            break
        else:
            print(f'# Empleado no encontrado!')

if __name__ == '__main__':
    diccionarios()