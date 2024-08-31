# Realiza un programa que convierta una frase ingresada por el
# usuario a minúsculas.

def cadenas():
    frase = input(f'# Ingresa una oración para convertirla en minusculas: ')
    fraseMinus = frase.lower()

    print(f'# Su frase en minusculas es: {fraseMinus}')
    
if __name__ == '__main__':
    cadenas()