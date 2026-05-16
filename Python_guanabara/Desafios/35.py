r1= int(input('Qual o comprimento do primeiro segmento? '))
r2= int(input('Qual o comprimento do segundo segmento? '))
r3= int(input('Qual o comprimento do terceiro segmento? '))

if (r1+r2)<r3:
    print('Os segmentos não podem formar um triângulo')
else:
    print('Os segmentos podem formar um triângulo')