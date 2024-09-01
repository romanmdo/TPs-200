# Crea un diccionario donde cada clave sea
# un nombre de materia (ej. "Matemáticas") y cada valor sea una lista de notas
# obtenidas en esa materia. Luego, muestra el promedio de notas para cada materia.

def diccionarios():
    l1 = [1, 2, 5, 4, 10]
    l2 = [10, 7, 9, 10, 10]

    materias = {
        'Matematicas' : l1,
    }

    for i in enumerate(l1):
        print(i)
        
        suma = 0
        suma = l1[i] + i

    print(f'# La suma es: {suma}')

if __name__ == '__main__':
    diccionarios()