import requests

teste = {"USDBRL":{"code":"USD","codein":"BRL","name":"Dólar Americano/Real Brasileiro","high":"4.8536","low":"4.776","varBid":"0.0075","pctChange":"0.16","bid":"4.819","ask":"4.822","timestamp":"1653424057","create_date":"2022-05-24 17:27:37"}}

resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/BTC-BRL")
data = resposta.json()
fulljson = data.get("BTCBRL")
low = fulljson.get("low")
print(low)