import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client(intents=discord.Intents.all())

def log(label):
    print(f'\n[+] ' + label)

@client.event
async def on_ready():
    log(f'{client.user} has connected to Discord!')

    servers = ''
    for guild in client.guilds:
        servers += guild.name + "; "

    log(f'{client.user} is connected to these guilds -> {servers}', )
        
    log(f'{client.user} is connected to {guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
    log(f'New message from {message.author} = {message.content}')

    if message.author == client.user:
        return

    if message.content.lower().startswith('cambio?'):
        await message.channel.send(f'<@{message.author.id}> Cagati addosso')

client.run(os.getenv('DISCORD_TOKEN'))
