from models import Persona 
from load import *
from db import read

def modify(datos):
    print('> Bienvenido al menu de modificar/eliminar, a continuacion, decide que deseas hacer!')
    time.sleep(.5)
    cont = 1
    op = int(input('1 - Modificar\n2 - Eliminar\n'))

    if op == 1:
        os.system('cls')
        print('> Bienvenido al menu de modificar, a continuacion, ingresa el DNI de la persona que deseas modificar!')
        time.sleep(.5)

        while cont > 0:
            searching = int(input('DNI: '))
            if searching < 0:
                print('- DNI no valido, ingresa otro porfavor')
                cont = 1
            else:
                break

        for i, value in enumerate(arreglo):
            if searching == value.dni:
                print('- Encontre a la persona!')
                time.sleep(.5)
                nombre = input('> Ingresa un nuevo Nombre: ')
                apellido = input('> Ingresa un nuevo Apellido: ')
                dni = int(input('> Ingresa un nuevo DNI: '))
                edad = int(input('> Ingresa una nueva Edad: '))

                value.nombre = nombre
                value.apellido = apellido
                value.dni = dni
                value.edad = edad

                print('- Persona modificada con exito!')
                print('_________________________________________________________________________')
            return 1

        '''
        for i, human in enumerate(datos):
            if searching == human.dni:
                data = open('data.txt','a')

                print('- Encontre a la persona!')
                time.sleep(.5)
                nombre = input('> Ingresa un nuevo Nombre: ')
                apellido = input('> Ingresa un nuevo Apellido: ')
                dni = int(input('> Ingresa un nuevo DNI: '))
                edad = int(input('> Ingresa una nueva Edad: '))

                human.nombre = nombre
                human.apellido = apellido
                human.dni = dni
                human.edad = edad

                for i, human in enumerate(arreglo):
                    human.dni = str(human.dni)
                    human.edad = str(human.dni)
        
                    data.write(f'{human.nombre},{human.apellido},{human.dni},{human.edad}\n')
                data.close()

                print('- Persona modificada con exito!')
                print('_________________________________________________________________________')
                return 1
        print('- La persona no existe Bc')
        '''