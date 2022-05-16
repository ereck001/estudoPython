

def Cadastro():
    customers = []
    res='S'
    while res == 'S':
        print('\n' * 20)

        cliente=[input('Infome o nome do cliente:'),
            input('Infome a cidade do cliente:'),
            int(input('Infome ano de nascimento do cliente:')),
            input('Infome o sexo do cliente:')]

        customers.append(cliente)
        print('\n'*20)

        res=input('Se deseja continuar digite S:').upper()
        return customers

def Mostar(customers):

    for item in customers:
        print('Nome: ', item[0])
        print('Cidade: ', item[1])
        print('Idade: ', 2022-item[2])
        print('Sexo: ', item[3])
        print('\n ','-=-'*30)