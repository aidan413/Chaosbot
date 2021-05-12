import discord
from discord.ext import commands
import os
import random


bot=commands.Bot(command_prefix='#')

def read_token():
    with open("token.txt","r") as f:
        lines=f.readlines()
        return lines[0].strip()

token=read_token()
invdict={}

@bot.event
async def on_ready():
    for guild in bot.guilds:
        invdict[guild.id]="a"
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_guild_join(guild):
    invdict[guild.id]="a"

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if (invdict[message.guild.id] in message.content.lower() and not(message.content.startswith('#c ') and not(' ' in message.content[3:]))):
        await message.channel.send('no')
        await message.delete()

    await bot.process_commands(message)
        
@bot.command(name='c')
async def change(ctx, args):
    if not(args[0].isalpha()):
        return
    
    invdict[ctx.guild.id]=(str(args[0]))
    await ctx.send('done')



bot.run(token)
