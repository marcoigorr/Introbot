
def handle_response(message) -> str:
    if message.content.lower() == 'cambio?':
        return f'<@{message.author.id}> Cagati addosso'
