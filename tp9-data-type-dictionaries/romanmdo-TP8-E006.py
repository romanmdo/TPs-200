# Crea un diccionario que almacene nombres de frutas y su
# cantidad disponible. Luego, cuenta cuántas frutas diferentes hay.

def diccionarios():
    diccionario = {
        'banana' : 2, 
        'manzana' : 3,
        'naranja' : 5
    }

    cont = 0
    print(f'# Bienvenido a la verduleria Condesa: ')
    print(f'# Elementos del diccionario: ')
    for i in diccionario:
        print(f'- {i} - Cantidad: {diccionario[i]}')
        cont += 1
    
    print(f'# La cantidad de frutas en el almacen Condesa, es de: {cont}')

if __name__ == '__main__':
    diccionarios()