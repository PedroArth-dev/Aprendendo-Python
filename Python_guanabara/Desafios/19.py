from random import choice
a= input('Primeiro aluno: ')
b= input('Segundo aluno: ')
c= input('Terceiro aluno: ')
d= input('Quarto Aluno: ')
lista= [a,b,c,d]

print('O aluno escolhido foi: {}'.format(choice(lista)))