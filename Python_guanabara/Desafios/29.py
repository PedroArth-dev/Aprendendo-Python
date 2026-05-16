v= int(input('Qual a velocidade do carro? '))
if v<80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    multa=(v-80)*7
    print('Velocidade excedida! Você foi multado em R${:.2f}'.format(multa))