

def cadastrar(inventario):
    resp = "S"
    while resp == "S":
        inventario[input('Digite o numero patrimonial: ')] = [
            input("Digite a data da ultima atualizacao: "),
            input("Digite a descricao: "),
            input("Digite o departamento: ")]
        resp = input("Digite S para continuar\n".upper())
def gravar(inv):
    with open(".inventario.csv", "a") as inv:
        for chave, valor in inv.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n ")
            print("Persistido com sucesso! ")
def mostrar():
    with open(".inventario.csv", "r") as inv:
        return inv.readlines()
def showMenu():
    opcao = int(input(
        "Digite:\n[1] para registrar o ativo\n[2] para persistir em arquivo\n[3] para exibir ativos armazenados\n"))
    return opcao