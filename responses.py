import discord


def handle_response(message):
    if message.content.lower() == 'cambio?':
        return f'<@{message.author.id}> Cagati addosso'

    if message.content[1:] == 'help':
        embed = discord.Embed(
            title="Introbot", url="https://github.com/marcoigorr/Introbot",
            description="Ciao sono Introbot! Il bot creato per **Emer**", color=discord.Color.blue()
        )
        embed.add_field(name="Ecco una lista dei miei comandi:", value="$play $leave", inline=True)

        return embed
