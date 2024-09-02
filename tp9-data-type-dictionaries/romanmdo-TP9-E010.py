# Crea un diccionario donde cada clave sea
# un nombre de materia (ej. "Matemáticas") y cada valor sea una lista de notas
# obtenidas en esa materia. Luego, muestra el promedio de notas para cada materia.

def average(y: list) -> int:
    resultado = 0
    for x in y:
        resultado += x
    return resultado / len(y)

def diccionarios():
    l1 = [1, 2, 5, 4, 10]
    l2 = [10, 7, 9, 10, 10]

    materias = {
        'Matematicas' : l1,
        'Programacion' : l2
    }

    for i in materias:
        print(f'{i}: {average(materias[i])}')

if __name__ == '__main__':
    diccionarios()