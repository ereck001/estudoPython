import random
import time

def cadastrar():
    itens=[]
    res='S'
    while res == 'S':
        itens.append(input('Digite o próximo nome: \n'))
        res=input('Para continuar digite S \n').upper()

    return itens

def sorteio(itens):
    for i in range(0, len(itens) - 1):
        print('\n' * 50)
        nome = input('Digite seu nome: ')
        daVez = random.randint(0, len(itens) - 1)

        if itens[daVez] == nome:
            daVez = random.randint(0, len(itens) - 1)

        print('{}, seu amigo secreto é {}'.format(nome, itens[daVez]))
        print('chame o próximo... ')
        time.sleep(3)
        input('Digite S para continuar: ').upper()
        print('\n' * 50)
        itens.pop(daVez)

    nome = input('Digite seu nome: ')
    print('{}, seu amigo secreto é {}'.format(nome, itens[0]))