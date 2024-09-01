# Escribe un programa que tenga un diccionario con
# datos de un libro (título, autor, año) y elimine el par clave-valor del año.

def diccionarios():
    libro = {
        'titulo' : 'Las aventuras de Mdo y Tto',
        'autor' : '20',
        'año' : '2do año'
    }

    del libro['año']
    
    print(f'# Elementos del diccionario: ')
    for i in libro:
        print(f'- {i}: {libro[i]}')

if __name__ == '__main__':
    diccionarios()