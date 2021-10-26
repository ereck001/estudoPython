import time
from datetime import datetime, date

ano = date.today().year
dia = date.today().day
mes = date.today().month
hora = datetime.now().strftime('%H:%M')
print('Hoje é dia {}/{}/{}'.format(dia, mes, ano))
print('E nesse momento o horário são  {} '.format(hora))

print('\033[1;31;40m==' * 25)
print('            10 TERMOS DE UMA PA')
print('==' * 25)
print('\033[m')

num = int(input('Informe o primeiro termo:'))
r = int(input('Infrome a razão sa PA:'))
print(num, end ='→')
for i in range(0,10):
    num += r
    print('{}'.format(num),end = '→')


