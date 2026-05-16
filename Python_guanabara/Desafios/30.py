num=int(input('Digite um número: '))
if num==0:
    print('O número 0 é neutro')
else:
    if num%2==0:
        print('O número {} é Par'.format(num))
    else:
        print('O número {} é Ímpar'.format(num))