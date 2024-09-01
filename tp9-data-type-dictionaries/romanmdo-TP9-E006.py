# Crea un diccionario que almacene nombres de frutas y su
# cantidad disponible. Luego, cuenta cuántas frutas diferentes hay.

def diccionarios():
    verduleria = {
        'banana' : 2, 
        'manzana' : 3,
        'naranja' : 5
    }

    cont = 0
    print(f'# Bienvenido a la verduleria Condesa: ')
    print(f'# Elementos de la verduleria: ')
    for i in verduleria:
        print(f'- {i} - Cantidad: {verduleria[i]}')
        cont += 1
    
    print(f'# La cantidad de frutas distintas en el almacen Condesa, es de: {cont}')

if __name__ == '__main__':
    diccionarios()