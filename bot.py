import discord
from discord.ext import commands
import os
import random




bot=commands.Bot(command_prefix='^',case_insensitive=True)

def read_token():
    with open("token.txt","r") as f:
        lines=f.readlines()
        return lines[0].strip()

token=read_token()
invdict={}
randict={}

@bot.event
async def on_ready():
    for guild in bot.guilds:
        invdict[guild.id]="a"
        randict[guild.id]=False
    print(f'{bot.user} has connected to discord')

@bot.event
async def on_guild_join(guild):
    invdict[guild.id]="a"
    randict[guild.id]=False

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    is_command=message.content.startswith('^') and message.content[1].isalpha()

    for i in invdict[message.guild.id]:
        if (i in message.content.lower() and not is_command):
            if randict[message.guild.id]==True:
                for letter in reversed(message.content):
                    if letter.isalpha():
                        invdict[message.guild.id]=letter.lower()
                        break
                    
            await message.channel.send('no')
            await message.delete()

    await bot.process_commands(message)
        
@bot.command(name='c')
async def change(ctx, args):
    if not(str(args).isalpha()):
        return
    
    invdict[ctx.guild.id]=(str(args))
    embed=discord.Embed(
        title='Key is now '+str(args),
        color=discord.Colour.red()
    )
    await ctx.send(embed=embed)

@bot.command(name='k')
async def key(ctx):
    embed=discord.Embed(
        title='Key is currently '+invdict[ctx.guild.id],
        color=discord.Colour.red()
    )
    await ctx.send(embed=embed)

@bot.command(name='rt')
async def random_on(ctx):
    
    randict[ctx.guild.id]=True
    embed=discord.Embed(
    title='Random key change on',
    color=discord.Colour.red()
    )
    await ctx.send(embed=embed)
    

@bot.command(name='rf')
async def random_off(ctx):
    randict[ctx.guild.id]=False
    embed=discord.Embed(
    title='Random key change off',
    color=discord.Colour.red()
    )
    await ctx.send(embed=embed)






bot.run(token)
