from load import *
from show import show
from search import search
from modify import modify
from close import close
from db import read

datos: list[str] = read()

def main():
    '''
    Funcion la cual spawnea el menu del programa
    '''

    print('> Welcome a Ranking with Splinter')
    time.sleep(.5)
    cont = 1
    while cont > 0:
        print('[1] - Load\n[2] - Show\n[3] - Search\n[4] - Modify/Deleted\n[5] - Go out\n')
        time.sleep(.5)
        menu = int(input('- Input your selection! '))
        
        if menu == 1:
            cont = 1
            load(datos)
        elif menu == 2:
            cont = 1
            show(datos)
        elif menu == 3:
            cont = 1
            search(datos)
        elif menu == 4:
            cont = 1
            modify(datos)
        elif menu == 5:
            cont = 0
            close()
            os.system('cls')
            print('> Thank You for ussed Splinter Ranked :)')
        else:
            print('> Say valid input!')

if __name__ == '__main__':
    main()

# · | Referencias |
# · # = Salida
# · - = Print or Intput
# · Importamos 'time' y 'os' para la estetica del programa
# · Importamos clase 'Persona' para que cada persona tenga sus atributos

# · if __name__ == '__main__': - Comprueba si el script se está ejecutando como programa principal.
# · los 'value.atributo' son los atributos de la persona que va a mostrar, los cuales estan almacenados en el arreglo!