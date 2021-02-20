import discord

client = discord.Client()
token = 1


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!announce'):
        await message.channel.send('Use this channel to interact with the Sig Sauce Game Bot.',
                                   'Games that are currently working:',
                                   '!tictactoe',
                                   '',
                                   '!tictactoe usage:',
                                   'Start a game with !tictactoe @player1 @player2.',
                                   'Place your marker with !place <1-9>')


client.run(token)
