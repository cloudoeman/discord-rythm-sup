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
  if ctx.content == 't':
    await ctx.channel.send('test')
  await bot.process_commands(ctx)


@bot.command()
async def ping(ctx):
  await ctx.send('pong')


@bot.command()    
async def cmd(ctx):
  await ctx.send('今実装しているコマンドは、\n'\
                  '[/syamu]\n'\
                  '[/rcmm]\n'\
                  '[/dsp]\n'\
                  'だで。')


async def reply(ctx):
  reply = f'{ctx.author.mention} とりあえず落ち着け、コマンドの一覧は[/cmd]だで' 
  await ctx.channel.send(reply)   


@bot.event
async def on_message(ctx):
  if bot.user in ctx.mentions: 
    await reply(ctx)
  await bot.process_commands(ctx) 


    
@bot.command()
async def syamu(ctx):
  await ctx.send('ウイイイイイイイッッッッス。どうも、シャムでーす。\
まぁ今日はオフ会、当日ですけども。\
えーとですね、まぁ集合場所の、えーイオンシネマに行ってきたんですけども、ただいまの時刻は1時を回りました。\
はい、ちょっと遅れて来たんですけどもね。えー11時ちょっとすぎくらいに、えーイオンシネマに行ったんですけども。\
ほんでーまぁイオンシネマの全体の動画を撮った後に行ったんですけども。スィー。\
ほんでーかれこれまぁ2時間くらい、えー待ったんですけども参加者は誰一人来ませんでした。ガチャ。\
誰一人来ることなかったですぅ。残念ながら。はい。\
一人くらい来るやろうなーと思ってたんですけども、スゥー、結局2時間くらい待っても誰一人来ませんでしたね、えぇ。\
でもね、でもオフ会のお知らせの動画にちらほらコメントあったんですけどもね。えー参加者の方の。\
なんだろう。なんで来なかったんでしょうかねー。\
まぁーもう一時間くらい待とうと思ったんですけども今日はね、えーまぁみんなとお昼ごはん食べるつもりだったし、\
あっ夜ご飯もみんなと一緒に食べようかなと思ってたんで今日は朝、パン一枚でございます。\
今日の朝食はパン一枚！\
なのでもう1時間待とうと思ったけどさすがにちょっと腹ペコなんで、えー今回のオフ会は残念ながら、こういう悲しい結果で終わりですね。')     

    
@bot.command()
async def pas(ctx):
  await ctx.send('グラップルを使うよ！')
    
    
@bot.command()
async def rcmm(ctx):
  await ctx.send('たまたま…たまたま…あの…俺が、おすすめ…俺らがおすすめ…私、我が家…がおすすめしますぅぅう')
  a = random.randint(0,3)
  if a == 0:
    await ctx.send('https://www.youtube.com/watch?v=H6ZlVto_oCs')
  elif a == 1:
    await ctx.send('https://www.youtube.com/watch?v=aokzZvBxHIU')
  elif a == 2:
    await ctx.send('https://www.youtube.com/watch?v=Qws2n9uBHaE')
  elif a == 3:
    await ctx.send('https://www.youtube.com/watch?v=D0GeBHWQtKY')
  await ctx.send('おもしろいけど、おもしろい')
    

@bot.command()
async def dsp(ctx):
  flag = True
  tt = 1
  while flag:
    async for m in ctx.history(limit=tt):
      if m.content[0:len("https://www.youtube")] == 'https://www.youtube' and m.author.bot:
        await m.delete()
        flag = False
        await ctx.send('これおすすめなんかな？わからんわ、確信がないわ、紹介するのやめとくわ')

      else:
        tt += 1    

        
@bot.command()
async def kill(ctx):
  await ctx.send('https://imgur.com/bc1rT5t')
        
        
    
bot.run(token)
