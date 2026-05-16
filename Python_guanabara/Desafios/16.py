from math import(floor)
num= float(input('Digite um número: '))
print('A parte inteira do número \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format(num, floor(num)))