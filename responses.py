
def handle_response(message) -> str:
    if message.content.lower() == 'cambio?':
        return f'<@{message.author.id}> Cagati addosso'

    if message.content == '$help':
        return f'Lo sapevi che Emer é sempre sul pezzo?'