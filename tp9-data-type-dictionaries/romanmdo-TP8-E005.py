# Escribe un programa que tenga un diccionario con
# datos de un libro (título, autor, año) y elimine el par clave-valor del año.

def diccionarios():
    diccionario = {
        'titulo' : 'Las aventuras de Mdo y Tto',
        'autor' : '20',
        'año' : '2do año'
    }

    del diccionario['Año']
    
    print(f'# Elementos del diccionario: ')
    for i in diccionario:
        print(f'- {i}: {diccionario[i]}')

if __name__ == '__main__':
    diccionarios()