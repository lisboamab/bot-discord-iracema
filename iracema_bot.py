import discord
from discord.ext import commands
from key_bot.token_bot import token
import requests
from moedas_validas import MoedasValidas


bot = commands.Bot("$")


@bot.event
async def on_ready():
    print("Estou pronto!")


@bot.event
async def on_message(message):
    # faz com que o bot não responda a si
    if message.author == bot.user:
        return

    # comando para o bot repetir uma mensagem e apagar a enviada pelo autor
    if "/double" in message.content:
        await message.channel.send(message.content.removesuffix("/double"))
        await message.delete()

    await bot.process_commands(message)


@bot.command(name="oi")
async def hello_model(ctx):
    name = ctx.author.name  # ctx é similar ao self e se refere ao proprio objeto
    response = (f"Olá {name}!!!")
    await ctx.send(response)

@bot.command() #mostra a cotação de uma moeda em relação ao real
async def cotacao(ctx, coin):
    try:
        resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{coin.upper()}-BRL")
        data = resposta.json() # {"USDBRL":{"code":"USD","codein":"BRL","name":"Dólar Americano/Real Brasileiro","high":"4.8536","low":"4.776","varBid":"0.0075","pctChange":"0.16","bid":"4.819","ask":"4.822","timestamp":"1653424057","create_date":"2022-05-24 17:27:37"}}
        fulljson = data.get(f"{coin}BRL")
        high = float(fulljson.get(f"high"))
        low = float(fulljson.get("low"))
        median_price = (high + low)/2

        if MoedasValidas.validadorDeMoeda(coin):
            await ctx.send(f"O valor do {coin} é {median_price:.2f} reais")
        else:
            await ctx.send(f"O valor {coin} é invalido")

    
    except:
        await ctx.send("Ops ... Deu algum erro!")

@bot.command(name="apresentação")
async def presentention_model(ctx):
    name = ctx.author.name
    presentation = (
        f'Olá {name}! O nosso modelo de apresentação é:\nQuem sou eu?\nDe onde sou?\nO que eu faço?\nO que te trouxe pro mundo da tecnologia?\nOlha eu no LinkedIn:\nOlha meu Github:')
    await ctx.send(presentation)


@bot.command(name="convite") #faz com que o bot envie o link de convite do servidor no chat
async def presentention_model(ctx):
    link_convite = "https://discord.gg/Y7T5Fegc7u"
    mensagem = (f'Convide seus amigos: {link_convite}')
    await ctx.send(mensagem)


bot.run(token)
