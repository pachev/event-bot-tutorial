from os import getenv
import discord
from discord.ext import commands

description = 'A seed bot that does nothing'
bot = commands.Bot(command_prefix='?', description=description)
token = getenv('BOT_TOKEN')


@bot.event
async def on_ready():
    print(bot.user.id)
    print(bot.user.name)
    print('---------------')
    print('This bot is ready for action!')

bot.run(token)
