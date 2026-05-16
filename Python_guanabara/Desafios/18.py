from math import radians, sin, cos, tan
a= float(input('Valor do ângulo em graus: '))

print('O seno, cosseno e a tangente do ângulo {}, são respectivamente {:.2f}, {:.2f}, {:.2f}.'.format(a, sin(radians(a)),cos(radians(a)),tan(radians(a))))