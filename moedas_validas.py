import json

#abre o arquivo .json 
with open('moedas.json') as moedas_json:
    moedas_dict = json.load(moedas_json) #json.load lê as informações do arquivo json e tranforma os dados para o tipo dict

    moedas_validas = list(moedas_dict.keys()) #lê as keys do dicionario e adiciona as mesmas em uma lista