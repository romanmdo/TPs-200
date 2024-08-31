# Escribe un programa que cuente cuántas veces
# aparece una letra específica en una palabra ingresada por el usuario.

def cadenas():
    frase = input(f'# Ingresa una frase: ')
    letra = input(f'# ¿Cual es la letra que deseas contar? (veces que aparece): ')
    cont = 0
    
    letraMinus = letra.lower()
    fraseMinus = frase.lower()

    for i in fraseMinus:
        if i == letraMinus:
            cont = cont + 1
    
    print(f'# La letra aparece {cont} veces')

if __name__ == '__main__':
    cadenas()