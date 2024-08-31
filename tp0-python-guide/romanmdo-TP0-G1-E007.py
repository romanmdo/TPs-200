def primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True

num = int(input('Num: '))
if primo(num):
    print('Es primo!')
else:
    print('Es compuesto!')