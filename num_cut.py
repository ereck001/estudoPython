
num = input('informe um número inteiro de até 4 digitos:')

print('esse número possui {} unidade(s)'.format(num[-1])) if len(num)>=1\
    else print('esse número possui 0 unidade(s))')
print('esse número possui {} dezena(s)'.format(num[-2])) if len(num)>=2\
    else print('esse número possui 0 dezena(s)')
print('esse número possui {} centena(s)'.format(num[-3])) if len(num)>=3\
    else print('esse número possui 0 centena(s)')
print('esse número possui {} milhare(s)'.format(num[-4])) if len(num)>=4\
    else print('esse número possui 0 milhare(s)')

