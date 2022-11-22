import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from datetime import datetime
import asyncio

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
    print(f'{Colors.HEADER}{datetime.now().strftime("%H:%M:%S")} {Colors.CYAN}[+]{Colors.END} ' + label)


async def send_message(message):
    try:
        response = responses.handle_response(message)

        if isinstance(response, discord.Embed):
            await message.channel.send(embed=response)
        else:
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

        log(f'{client.user} is connected to {guild.name} (id: {guild.id})')

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
    async def help(ctx):
        await send_message(ctx)

    @client.event
    async def on_voice_state_update(member, before, after):
        if not before.channel and after.channel and (member.id == 436886851605889036 or member.id == 425283882628284416):  # Emer ID e marcoigorr
            channel = client.get_channel(962076175180632105)  # gente che parla 1 702594762095591424
            voice = await channel.connect()
            source = FFmpegPCMAudio('audio/Intro.wav')
            player = voice.play(source)

            while True:
                await asyncio.sleep(1)
                if voice.is_playing() or voice.is_paused():
                    continue

                await voice.disconnect()

    @client.command(pass_context=True)
    async def play(ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('audio/Intro.wav')
            player = voice.play(source)

            while True:
                await asyncio.sleep(1)
                if voice.is_playing() or voice.is_paused():
                    continue

                await voice.disconnect()

        else:
            await ctx.send('Non sei connesso a nessun canale vocale.')

    @client.command(pass_context=True)
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()

        else:
            await ctx.send('Non sono in un canale vocale')

    client.run(_token)
