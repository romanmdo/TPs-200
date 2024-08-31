# Crea un programa que divida una frase en palabras individuales y
# luego las imprima en líneas separadas.

def cadenas():
    frase = input(f'# Ingresa una frase para dividir sus letras: ')
    for i in frase:
        print(i)

if __name__ == '__main__':
    cadenas()