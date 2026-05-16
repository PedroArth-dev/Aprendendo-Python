'''nome= input()
if nome == 'Gustavo':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal')
print('Bom dia {}'.format(nome))
'''

n1= float(input('Digite sua primeira nota: '))
n2=float(input('Digite a sua segunda nota: '))
if n1>10:
    print('Valor inválido')
if n2>10:
    print('Valor inválido')
else:
    m=(n1+n2)/2
    print('Sua média foi {:.1f}'.format(m))
    if m >= 6.0:
        print('Sua média foi boa! Parabéns!')
    else:
        print('Sua média foi ruim! Estude mais!')
#Fui adptando o código para evitar possíveis erros do usuário.
