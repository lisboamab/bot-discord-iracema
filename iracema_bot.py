import discord
from discord.ext import commands
from key_bot.token_bot import token


bot = commands.Bot("$")

@bot.event
async def on_ready():
    print("Estou pronto!")

@bot.event
async def on_message(message):
    #faz com que o bot não responda a si
    if message.author == bot.user:
        return
    
    #comando para o bot repetir uma mensagem e apagar a enviada pelo autor
    if "/double" in message.content:
        await message.channel.send(message.content.removesuffix("/double"))
        await message.delete()

    await bot.process_commands(message)
    


@bot.command(name="oi")
async def hello_model(ctx):
    name = ctx.author.name #ctx é similar ao self e se refere ao proprio objeto
    response = (f"Olá {name}!!!")
    await ctx.send(response)

@bot.command(name="apresentação")
async def presentention_model(ctx):
    name = ctx.author.name
    presentation = (f'Olá {name}! O nosso modelo de apresentação é:\nQuem sou eu?\nDe onde sou?\nO que eu faço?\nO que te trouxe pro mundo da tecnologia?\nOlha eu no LinkedIn:\nOlha meu Github:')
    await ctx.send(presentation)

@bot.command(name="convite")
async def presentention_model(ctx):
    link_convite = "https://discord.gg/Y7T5Fegc7u"
    mensagem = (f'Convide seus amigos: {link_convite}')
    await ctx.send(mensagem)


bot.run(token)
