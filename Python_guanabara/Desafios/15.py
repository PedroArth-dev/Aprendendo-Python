dias= int(input('Por quantos dias o veículo foi alugado? '))
km= int(input('Quantos km foram percorridos? '))

v1= dias*60
v2= km*0.15
vt= v1+v2

print('O carro foi alugado por {} dias e percorreu {}km. \nO valor total a ser pago é de R${:.2f}'.format(dias,km,vt))