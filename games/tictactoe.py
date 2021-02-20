from discord.ext import commands
import discord
import random

client = commands.Bot(command_prefix='!')
token = 'ODEyNzIzMjI3MjYzNjMxMzYw.YDE5fQ.cqfiOKoi3fGA-wLAP3jIG_EtETo'

player1 = ''
player2 = ''
turn = ''
game_over = True
count = 0

board = []

winning_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global player1
    global player2
    global turn
    global game_over
    global count

    if game_over:
        global board
        board = [':white_large_square:', ':white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:']
        turn = ''
        game_over = False
        count = 0

        player1 = p1
        player2 = p2

        #  print the board
        line = ''
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += ' ' + board[x]
                await ctx.send(line)
                line = ' '
            else:
                line += ' ' + board[x]

        #  determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send('It is <@' + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send('It is <@' + str(player2.id) + ">'s turn.")
    else:
        await ctx.send('A game is already in progress! Finish it before starting a new one.')


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global game_over

    if not game_over:
        mark = ''
        if turn == ctx.author:
            if turn == player1:
                mark = ':regional_indicator_x:'
            elif turn == player2:
                mark = ':o2:'
            if 0 < pos < 10 and board[pos - 1] == ':white_large_square:':
                board[pos - 1] = mark
                count += 1

                #  print board
                line = ''
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += ' ' + board[x]
                        await ctx.send(line)
                        line = ' '
                    else:
                        line += ' ' + board[x]

                check_winner(winning_conditions, mark)
                print(count)
                if game_over:
                    await ctx.send(mark + ' wins!')
                elif count >= 9:
                    game_over = True
                    await ctx.send("It's a tie!")

                #  switch turn
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1

            else:
                await ctx.send('Be sure to choose a number between 1 and 9 and an unmarked tile.')
        else:
            await ctx.send('It is not your turn')
    else:
        await ctx.send('Please start a new game using the !tictactoe command.')


def check_winner(winning_conditions, mark):
    global game_over
    for condition in winning_conditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            game_over = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please mention 2 players for this command.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Please make sure to mention/ping players (ie. <@812723227263631360).')


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please enter a position you would like to mark.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Please make sure to a correct number (ie. 1 through 9).')


client.run(token)
