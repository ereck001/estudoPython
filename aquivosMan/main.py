


# with open("teste.txt",'w') as arquivo:
#
#     arquivo.write('novo teste de texto no arquivo')
#
# with open("teste.txt",'r') as arquivo:
#
#    content = arquivo.read()
#    print(content)
# with open("pagina.html", "w") as pagina:
#     pagina.write("<head> <style>h3{ text-align:center;}</style> </head>")
#     pagina.write("<body> <h1> Esta é um teste para página WEB </h1>")
#     pagina.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto:  </h2>")
#     pagina.write("<h3>")
#     nome=""
#     while nome!="SAIR":
#         nome = input("Digite um nome ou SAIR: ").upper()
#         if nome!="SAIR":
#             pagina.write("<br>"+nome)
#     pagina.write("</h3></body>")

with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.read()
print("Tipo de dado da variável",type(conteudo))
print("Conteúdo do arquivo:",conteudo)






