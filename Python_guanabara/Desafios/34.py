s= float(input('Digite seu salário: R$'))
if s<=1250.00:
    a2= 15/100
    sa2= s+s*a2
    print('Seu salário após aumento ficará R${:.2f}'.format(sa2))
else:
    a1= 10/100
    s2= s+s*a1
    print('Seu salário após aumento ficará R${:.2f}'.format(s2))