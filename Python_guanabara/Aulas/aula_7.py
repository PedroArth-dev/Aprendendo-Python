#operadores em python
n= int(input('Um valor: '))
m= int(input('Outro valor: '))

x= n+m
y= n-m
z= n*m
p= n/m
o= n//m #divisão sem resto
l= n%m #resto da divisão
h= n**m #potenciação

#REGRAS DE PRECEDÊNCIAS
'''
Em primeiro o python resolverá o que estiver dentro dos parênteses

depois a potenciação

multiplição e divisões

e por último soma e subtração (exatamente como na matemática básica.)
'''
print('A soma é {}, \n o produto é {}, \n e a divisão {}' .format(x,z,p))
print('A divisão inteira {} e a potência é {}'.format(o,h))