import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl

import responses


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log(label):
    print(f'{Colors.CYAN}[+]{Colors.END} ' + label)


async def send_message(message):
    try:
        response = responses.handle_response(message)
        await message.channel.send(response)
    except Exception as e:
        pass


def run_discord_bot():
    load_dotenv()
    _token = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.all()
    client = commands.Bot(command_prefix='$', intents=intents)

    client.remove_command('help')

    @client.event
    async def on_ready():
        log(f'{client.user} has connected to Discord!')
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name="$help", type=3))

        servers = ''
        for guild in client.guilds:
            servers += guild.name + "; "

        log(f'{client.user} is connected to these guilds -> {servers}')

        log(f'{client.user} is connected to {guild.name}(id: {guild.id})')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        log(f'{username} said: \'{user_message}\' ({channel})')

        await send_message(message)

        await client.process_commands(message)

    @client.command()
    async def hello(ctx):
        await ctx.send('Ciao')

    @client.command(pass_context=True)
    async def play(ctx, url:str):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()

        else:
            await ctx.send('Non sei connesso a nessun canale vocale.')

    @client.command(pass_context=True)
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send('Ho lasciato il canale vocale')
        else:
            await ctx.send('Non sono in un canale vocale')

    client.run(_token)
