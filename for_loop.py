from datetime import datetime, date

ano = date.today().year
dia = date.today().day
mes = date.today().month
hora = datetime.now().strftime('%H:%M')
print('Hoje é dia {}/{}/{}'.format(dia, mes, ano))
print('E nesse momento o horário são  {} '.format(hora))

print('\033[1;31;40m=X=\033[m' * 20)

for i in range(20,0,-2):
    print('temos {} earplugs em estoque'.format(i))
print('\033[1;31;40macabou\033[m')
