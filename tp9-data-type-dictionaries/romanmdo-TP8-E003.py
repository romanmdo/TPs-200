# Crea un diccionario vacío y permite al usuario
# agregar una clave "nombre" con su nombre como valor.

def diccionarios():
    diccionario = {}

    diccionario['Nombre'] = input('# Ingresa el nombre: ')
    print(f'- Nombre: {diccionario["Nombre"]}')

if __name__ == '__main__':
    diccionarios()