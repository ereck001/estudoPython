import json

with open('rNm.json','r') as arq:
    rickNmorty = json.load(arq)
for i in range(0,len(rickNmorty['results'])):

    print('The {} is a '.format(rickNmorty['results'][i]['name']),end="")#rickNmorty['results'][i]['species'],rickNmorty['results'][i]['gender'])
    print(rickNmorty['results'][i]['species'], end="")
    print(' {}'.format(rickNmorty['results'][i]['gender']))
   # print(len(rickNmorty['results']))
