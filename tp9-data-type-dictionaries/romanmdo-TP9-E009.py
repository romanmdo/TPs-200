# Iteración sobre diccionarios: Escribe un programa que recorra un diccionario de
# productos (clave: nombre del producto, valor: precio) y muestre cada producto con
# su precio.

def diccionarios():
    producto = {
        'Tanque de Condesa' : 500,
        'Tanque de Morgan' : 800,
        'Tanque de Roca Rosa' : 400
    }

    print(f'# Elementos a la venta: ')
    for i in producto:
        print(f'- {i}: Precio: ${producto[i]}')


if __name__ == '__main__':
    diccionarios()