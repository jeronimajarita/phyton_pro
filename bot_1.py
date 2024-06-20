from tecnico import gen_pass
from tecnico import flip_coin
import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$hola'):
        await message.channel.send("hola soy boot en que puedo ayudarte")
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(gen_pass(int(message.content)))

client.run("MTI1MDk4NTgxMjkyMTY3OTg4Mg.GVBVv8.pfDpBuQ_H3Ct2gMG2gV7GgzXvL24Eh3s-QEXyQ")
