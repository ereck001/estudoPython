from funcoes import *


inventario={}

opcao=showMenu()

while opcao>0 and opcao<4:
    if opcao==1:
        cadastrar(inventario)
    elif opcao==2:
       gravar(inventario)
    elif opcao==3:
        resultado = mostrar()
        for linha in resultado:
            print(linha[(linha.find(";")+1):-1])
    opcao=showMenu()

