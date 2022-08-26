import discord
from discord.ext import commands
from random import randint, random

description = '''Bot de jeu du serveur Citadelle'''
prefix = '?'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def roll(ctx, limit=6):
    result = f"Vous avez tirez : {str(randint(1,limit))}"
    await ctx.send(result)

@bot.command()
async def createRole(ctx, name):
    author = ctx.message.author
    await bot.create_role(author.server, name="Default")

@bot.command()
async def addRole(ctx, role, pseudo):
    pass

bot.run('MTAxMjM5MzU4MjU2MjM4NTk3MA.Gl0SpF.63vp2vdjIZy6xZNiLPqNlBlhUiI8kqTgX5xElk')