from math import hypot
a= float(input('Medida A: '))
b= float(input('Medida B: '))

print('Dados os catetos \033[1;31m{}\033[m e \033[1;31m{}\033[m, a hipotenusa do triângulo é \033[1;32m {:.2f} \033[m'.format(a,b,hypot(a,b)))