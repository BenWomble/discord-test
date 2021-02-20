import discord

client = discord.Client()
token = 'ODEyNzIzMjI3MjYzNjMxMzYw.YDE5fQ.seeMnlkisCC4uzXvtY4lpbXbFzg'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


client.run(token)
