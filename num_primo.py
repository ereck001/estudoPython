num = int(input('Informe o número:'))

cont = 0

for i in range(num,1,-1):
    if num % i == 0:
        print('{} é divisivel por {}'.format(num,i))
        cont += 1
if cont == 1:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))

