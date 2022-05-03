nome=input("Digite seu nome:")
idade=int(input("Digite sua idade"))

if idade<18 and idade>15:
    print("Voto não obrigatório")
elif idade>=18:
    print("Voto obrigatório")
else:
    print("Não vota")