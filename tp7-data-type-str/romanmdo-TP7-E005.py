# Crea un programa que solicite al usuario ingresar una oración y luego
# imprima los primeros cinco caracteres de la misma.

def cadenas():
    cadena = input(f'# Ingresa una oración: ')
    caracterUno = cadena[0]
    caracterDos = cadena[1]
    caracterTres = cadena[2]
    caracterCuatro = cadena[3]
    caracterCinco = cadena[4]

    print(f'Los 5 primeros caracteres fueron: {caracterUno} {caracterDos} {caracterTres} {caracterCuatro} {caracterCinco}')
    
if __name__ == '__main__':
    cadenas()