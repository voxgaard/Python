import discord
from discord.ext import commands

client = commands.Bot(command_prefix="=", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("GT_Bot has returned to this realm.")

@client.command()
async def ping(ctx):
    await ctx.send("Boop")

client.run("MTA3MzI3OTMzOTU1MjA0NzExNQ.G2CQe1.nbmLMfJ3ZG6IPVfLCf8_wJjFgIfyyK1Sjq2c9g")
