

participantes=[]

res = 'S'
while res == 'S':
    piloto = {"nome": input("nome: "), "carro": input("carro: ")}

    participantes.append(piloto)

    res = input('Digite S para continuar: \n').upper()

for i in range(0,len(participantes)):
    print('O carro do piloto {} é um {}'.format(participantes[i]['nome'],participantes[i]['carro']))

