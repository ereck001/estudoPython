import random
print('Tente adivinhar o número!\n')
num = int(input('Digite um número inteiro de zero a cinco:\n'))
res = random.randint(1,5)

if num > 0 and num <=5:
    print('Parabéns, você acertou!')if num == res else print('Você errou!')
else:
    print('Digite um número válido')
