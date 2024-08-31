# Haz programa que convierta una tupla de caracteres en un string.

def tuplas():
    tupla = ('C', 'o', 'n', 'd', 'e', 's', 'a')
    tuplaText = ''
    
    for i in range(len(tupla)):
        tuplaText += tupla[i]

    print(f'> Nos vamos a... {tuplaText}!')

if __name__ == '__main__':
    tuplas()