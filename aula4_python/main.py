import os

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'

while resposta == 'S':
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite S para continuar: ").upper()
    os.system('clear')
    print("\n")

os.system('cls')
print("\n")

for i in range(0,len(equipamentos)):
    print("Equipamento: ", i )
    print("Nome..........: ",equipamentos[i])
    print("Valor.........: ", valores[i])
    print("Serial........: ", seriais[i])
    print("Departamento  : ", departamentos[i])





#for equipamento in equipamentos:
#    print("Equipamento: ", equipamento)