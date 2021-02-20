import discord
import random
import main

player1 = ''
player2 = ''
turn = ''
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@main.client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global player1
    global player2
    global turn
    global gameOver
    global count

    if gameOver:
        global board
        board = [':white_large_square:', ':white_large_square:', ':white_large_square:'
                 ':white_large_square:', 'white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:']
        turn = ''
        gameOver = False
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


@main.client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count

    if not gameOver:
        mark = ''
        if turn == ctx.author:
            pass
        else:
            await ctx.send('It is not your turn')
    else:
        await ctx.send('Please start a new game using the !tictactoe command.')
