import time
from datetime import datetime, date

ano = date.today().year
dia = date.today().day
mes = date.today().month
hora = datetime.now().strftime('%H:%M')
print('Hoje é dia {}/{}/{}'.format(dia, mes, ano))
print('E nesse momento o horário são  {} '.format(hora))

print('\033[1;31;40m==' * 25)
print('            Palíndromo')
print('==' * 25)
print('\033[m')
# print('{}'.format(num),end = '→')
entrada = input('Informe uma frase:').upper()
frase = entrada.split()
novaFrase = ''.join(frase)
invert = novaFrase[::-1]
print('O inverso de {} é {}'.format(novaFrase,invert))
if invert == novaFrase:
    print('temos um Palíndromo!')
