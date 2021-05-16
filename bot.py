import discord
from discord.ext import commands
import os
from random import randint




bot=commands.Bot(command_prefix='^',case_insensitive=True)


token=os.getenv('LTOKEN')
invdict={}
randict={}
enadict={}
commlist=['^c', '^k', '^r','^e','^s']

@bot.event
async def on_ready():
    for guild in bot.guilds:
        invdict[guild.id]="a"
        randict[guild.id]=False
        enadict[guild.id]=True
    print(f'{bot.user} has connected to discord')

@bot.event
async def on_guild_join(guild):
    invdict[guild.id]="a"
    randict[guild.id]=False
    enadict[guild.id]=True

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    is_command=message.content[0:2] in commlist

    if is_command and message.content[0:2]!='^c':
        if len(message.content)>3:
            is_command=False

    if is_command and message.content[0:2]=='^c':
        if message.content[2]!=' ':
            is_command=False
        
        if not message.content[3:].isalpha():
            is_command=False

    if enadict[message.guild.id]:
        for i in invdict[message.guild.id]:
            if (i in message.content.lower() and not is_command):
                if randict[message.guild.id]==True:
                    alph=False
                    while not alph:
                        letter=message.content[randint(0,len(message.content)-1)].lower()
                        if letter.isalpha():
                            invdict[message.guild.id]=letter
                            alph=True

                        
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

@bot.command(name='r')
async def random(ctx):
    
    if not randict[ctx.guild.id]:
        randict[ctx.guild.id]=True
        embed=discord.Embed(
        title='Random key change on',
        color=discord.Colour.red()
        )
        await ctx.send(embed=embed)

    elif randict[ctx.guild.id]:
        randict[ctx.guild.id]=False
        embed=discord.Embed(
        title='Random key change off',
        color=discord.Colour.red()
        )
        await ctx.send(embed=embed)

@bot.command(name='e')
async def enable(ctx):
    
    if not enadict[ctx.guild.id]:
        enadict[ctx.guild.id]=True
        embed=discord.Embed(
        title='Bot has been turned on',
        color=discord.Colour.red()
        )
        await ctx.send(embed=embed)

    elif enadict[ctx.guild.id]:
        enadict[ctx.guild.id]=False
        embed=discord.Embed(
        title='Bot has been turned off',
        color=discord.Colour.red()
        )
        await ctx.send(embed=embed)

@bot.command(name='s')
async def status(ctx):

    if enadict[ctx.guild.id]:
        embed=discord.Embed(
        title='Bot on',
        color=discord.Colour.red()
        )
        await ctx.send(embed=embed)

    else:
        embed=discord.Embed(
        title='Bot off',
        color=discord.Colour.red()
        )
        await ctx.send(embed=embed)

    


bot.run(token)
