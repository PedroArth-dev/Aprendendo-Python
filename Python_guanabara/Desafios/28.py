from random import randint
from time import sleep
print('-=-'*20)
print('Estou pensando em um número entre 0 e 5...')
sleep(3)
print('-=-'*20)
num= int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
a= randint(0,5)
if num == a:
    print('Parabéns você acertou!!')
else:
    print('Você errou eu pensei no número {}'.format(a))