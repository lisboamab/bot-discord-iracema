import json

#abre o arquivo .json 
with open('moedas.json') as moedas_json:
    moedas_dict = json.load(moedas_json) #json.load lê as informações do arquivo json e tranforma os dados para o tipo dict

    moedas_validas = list(moedas_dict.keys()) #lê as keys do dicionario e adiciona as mesmas em uma lista

class MoedasValidas():
    def __init__(self, moeda) -> None:
        self.moeda = moeda
    
    def validadorDeMoeda(self) -> bool:
        if self.moeda in moedas_validas:
            return True
        else:
            return False