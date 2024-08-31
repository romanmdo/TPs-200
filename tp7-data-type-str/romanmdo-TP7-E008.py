# Escribe un programa que tome una oración, reemplace todas
# las ocurrencias de una palabra específica por otra palabra, y luego imprima la nueva
# oración.

def cadenas():
    oracion = input(f'# Ingresa una oración: ')
    palabra = input(f'# Ingrese la palabra que desea cambiar: ')
    nuevaPalabra = input(f'# Ingrese la nueva palabra: ')

    oracionLower = oracion.lower()
    palabraLower = palabra.lower()
    nuevaLower = nuevaPalabra.lower()

    oracionUltimatum = oracionLower.replace(palabraLower, nuevaLower)
    print(f'# Su antigua oración es: {oracion}')
    print(f'# Su oración actualizada es: {oracionUltimatum}')

if __name__ == '__main__':
    cadenas()