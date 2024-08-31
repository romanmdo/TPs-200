from load import *

def close():
    data = open('data.txt','a')
    for i, value in enumerate(arreglo):
        value.dni = str(value.dni)
        value.edad = str(value.dni)
        
        data.write(f'{value.nombre},{value.apellido},{value.dni},{value.edad}\n')
    data.close()