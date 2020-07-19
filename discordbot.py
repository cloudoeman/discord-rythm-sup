from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

async def on_message(ctx):
    if ctx.author.bot:
      return

    if ctx.content == 't':
      await ctx.channel.send('test')
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    

    
bot.run(token)
