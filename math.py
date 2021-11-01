import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Online")
    print(client.user.name)

#LETS CODE MATH COMMANDS
#passing two values in cmd
@client.command()
async def add(ctx, a: int, b: int):
    embed = discord.Embed(title="Correct answer :",description=a+b,color=0x9208ea)
    embed.set_footer(text="I Was Framed Calculator")
    await ctx.send(embed=embed)

#NOW MULTIPLY CMD
@client.command()
async def multiply(ctx, a: int, b: int):
    embed = discord.Embed(title="Correct answer :",description=a*b,color=0x9208ea)
    embed.set_footer(text="I Was Framed Calculator")
    await ctx.send(embed=embed)

#NOW DIVIDE CMD
@client.command()
async def divide(ctx, a: int, b: int):
    divide25 = (a/b)
    embed = discord.Embed(title="Correct answer :",description=str(divide25),color=0x9208ea)
    embed.set_footer(text="I Was Framed Calculator")
    await ctx.send(embed=embed)

#EVERYTHING DONE! LETS CHECK

client.run('TOKEN')