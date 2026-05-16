nome= str(input('Seu nome completo: ')).strip()

print('Seu nome em maiúsculas fica: {}'.format(nome.upper()))

print('Seu nome em minúsculas fica: {}'.format(nome.lower()))

print('Seu nome tem {} Letras'.format(len(nome)-nome.count(' ')))