# Escribe un programa que pida al usuario ingresar una frase y
# la convierta completamente a mayúsculas.

def cadenas():
    frase = input(f'# Ingresa una oración para convertirla en mayusculas: ')
    fraseMayus = frase.upper()

    print(f'# Su frase en mayusculas es: {fraseMayus}')
    
if __name__ == '__main__':
    cadenas()