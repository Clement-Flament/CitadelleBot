import discord
from discord.ext import commands
from discord.utils import get
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
async def addrole(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')

@bot.command(pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

@bot.command()
async def new(ctx, arg1, arg2):
    guild = ctx.message.guild

    category = await ctx.guild.create_category(arg1)
    await guild.create_text_channel(arg2, category=category)

bot.run('TOKEN')
