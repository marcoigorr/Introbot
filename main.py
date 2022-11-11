import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client(intents=discord.Intents.default())

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
async def on_message():
    if message.content.startswith('cambio?'):
        await message.channel.send('Cagati addosso')

client.run(os.getenv('DISCORD_TOKEN'))
