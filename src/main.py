from logging import NullHandler, fatal
import os
from discord.ext import commands
from discord import permissions
import discord


bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 892820234992504852  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):  
    await ctx.send(ctx.author.name)

@bot.command()
async def count(ctx):
    for i in bot.get_all_members():
        print(i)
    await ctx.send("end")

@bot.command()
async def admin2(ctx, arg):
    ctx.create_role

@bot.command()
async def admin(ctx, arg):
    for role in ctx.guild.roles :
        if role.name == "Admin" :
            return role
    newRole = await ctx.guild.create_role(name="Admin" ,permissions=discord.Permissions(permissions=22))
    await bot.add_roles(arg, newRole)

@bot.command()
async def ban(ctx, arg):
    ctx.member.ban(arg)

@bot.command()
async def xkcd(ctx):
    

@bot.command()
async def poll(ctx, *arg):
    str = "@here "
    
    b = True

    c = 0

    for i in arg:
        c+= 1
        b = False
        str = str +" " + i
    if b or (c == 1):
        str = ":thumbsdown:"
    await ctx.send(str)

IsTicTacToe = False
TicTacToePlayer1 = 0
TicTacToePlayer2 = 0

@bot.command()
async def tictactoe(ctx, player1, player2):
    await ctx.send("welcome, " + player1 + "you play first, play with !play and place with ur for up right, um for up middle, ul for up left, mr for midlle right, mm for midle midle, ml for midlle left, dr for down right, dm for down middle and dl for down left")


@bot.command()
async def play(ctx, move):
    if not IsTicTacToe :
        await ctx.send("No TicTacToe running, type !tictactoe <player1> <player2> for playing")
        return
    if ctx.author != TicTacToePlayer1 or ctx.author != TicTacToePlayer2:
        await ctx.send("your not a player")
        return
    if ctx.author != TicTacToePlayer1 :
        await ctx.send("it's not your turn")
        return
    
    
    
    

token = ""
bot.run(token)  # Starts the bot