d=float(input('Quantos quilômetros você vai viajar? '))
print('Você está prestes a fazer uma viagem de {}Km'.format(d))
if d<=200:
    p1=0.5*d
    print('O valor da sua passagem será R${:.2f}'.format(p1))
else:
    p2=0.45*d
    print('O valor da sua passagem será R${:.2f}'.format(p2))