# Crea un diccionario con tres elementos que
# representen un producto (por ejemplo, nombre, precio y cantidad) y luego
# imprímelo.

def diccionarios():
    producto = {
        'nombre': 'MDO',
        'precio': 912,
        'cantidad': 5
    }

    print(f'# Elementos del diccionario: ')
    for i in producto:
        print(f'- {i}: {producto[i]}')


if __name__ == '__main__':
    diccionarios()