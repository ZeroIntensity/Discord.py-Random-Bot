import discord
import os
import dotenv
import traceback
import random
from discord.ext import commands
client=commands.Bot(command_prefix='/random ')
client.remove_command("help")
dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
@client.event
async def on_ready():
  await client.wait_until_ready()
  print(f"Logged in as {client.user} ({client.user.id})")
  await client.change_presence(activity=discord.Activity(name="/random help", type=discord.ActivityType.playing))
@client.command()
async def help(ctx):
  try:
    embed=discord.Embed(color=0x00ff00)
    embed.title='Help!'
    embed.description='Use ``/random choice`` to choose a random choice!\nUse ``/random number`` to choose a random number!'
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.timestamp=(ctx.message.created_at)
    await ctx.send(embed=embed)
    return
  except Exception as error:
    embed=discord.Embed(color=0x00ff00)
    embed.title='Error'
    embed.description=f"```\n{traceback.format_exc()}\n```"
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.timestamp=(ctx.message.created_at)
    await ctx.send(embed=embed)
@client.command()
async def number(ctx, args=None, args2=None):
  try:
    embed=discord.Embed(color=0x00ff00)
    embed.title='Random Number'
    embed.description=random.randint(int(args),int(args2))
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.timestamp=(ctx.message.created_at)
    await ctx.send(embed=embed)
    return
  except Exception as error:
    embed=discord.Embed(color=0xff0000)
    embed.title='Error'
    embed.description=f"```\n{traceback.format_exc()}\n```"
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.timestamp=(ctx.message.created_at)
    print(f'Exception in command number: \n{traceback.format_exc()}')
    await ctx.send(embed=embed)
@client.command()
async def choice(ctx, *, args=None):
  try:
    choices = []
    choices.extend(args.split("/"))
    embed=discord.Embed(color=0x00ff00)
    embed.title='Random Choice'
    embed.description=f'{random.choice(choices)}'
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.timestamp=(ctx.message.created_at)
    await ctx.send(embed=embed)
  except Exception as error:
    embed=discord.Embed(color=0xff0000)
    embed.title='Error'
    embed.description=f"```\n{traceback.format_exc()}\n```"
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.timestamp=(ctx.message.created_at)
    print(f'Exception in command choice: \n{traceback.format_exc()}')
    await ctx.send(embed=embed)
client.run(TOKEN)
