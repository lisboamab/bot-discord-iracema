import json

#abre o arquivo .json 
with open('moedas.json') as moedas_json:
    moedas_dict = json.load(moedas_json) #json.load lê as informações do arquivo json e tranforma os dados para o tipo dict

    lista_keys = list(moedas_dict.keys()) #lê as keys do dicionario e 
    print(lista_keys)
    print(type(lista_keys))