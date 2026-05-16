#Como colocar cores no terminal?

#fontes
#0 none, 1 bold, 4 underline, 7 negative

#texto
#30 cinza, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 ciano, 37 branco

#back
#40 cinza, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 roxo, 46 ciano, 47 branco
print('\033[1;32m Olá, Mundo!\033[m')
nome= 'Pedro'
print('Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;31m', nome, '\033[m'))