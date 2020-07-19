import discord
import os
import traceback
import random

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


    
@client.event
async def on_message(ctx):
    if ctx.author.bot:
      return

    if ctx.content == 't':
      await ctx.channel.send('test')
    


    
client.run(token)
