
inventario=[]
resposta = "S"
while resposta == "S":

    equipamento=[input("Equipamento: "),float(input("Valor: ")),input("Serial: "),input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Para continuar, digite (S):").upper()

for elemento in inventario:
    print("Nome:.........: ", equipamento[0])
    print("Valor.........: ", equipamento[1])
    print("Serial........: ", equipamento[2])
    print("Departamento..: ", equipamento[3])

busca=input("Digite o nome do equimamento que deseja buscar:")
for elemento in inventario:
    if busca == equipamento[0]:
        print("Nome:.........: ", equipamento[0])
        print("Valor.........: ", equipamento[1])
        print("Serial........: ", equipamento[2])
        print("Departamento..: ", equipamento[3])

depreciacao=input("Digite o nome do equimamento a ser depreciado: ")
for elemento in inventario:
    if depreciacao == equipamento[0]:
        print("Valor antigo: ",elemento [1])
        elemento[1]=elemento[1]*0.9
        print("Novo valor: ", elemento[1])

for elemento in inventario:
    print("Nome:.........: ", equipamento[0])
    print("Valor.........: ", equipamento[1])
    print("Serial........: ", equipamento[2])
    print("Departamento..: ", equipamento[3])

valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))