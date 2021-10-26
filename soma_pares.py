valIni = 0
for i in range (1,7):

    num = int(input('imforme o {}º número:'.format(i)))
    if num % 2 == 0 :
        valIni += num

print(valIni)
