import os

import traceback

import random

import discord
from discord.ext import commands

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
    
@client.event
async def on_message(ctx):
    if ctx.author.bot:
      return

    if ctx.content == 't':
      await ctx.channel.send('test')
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
client.run(token)
bot.run(token)
