import os

import traceback

import random

import discord
from discord.ext import commands

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
    
@bot.event
async def on_message(ctx):
    await process_commands()
    if ctx.content == 't':
      await ctx.channel.send('test')
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
bot.run(token)
