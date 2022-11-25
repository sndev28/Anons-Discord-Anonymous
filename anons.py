import discord
from discord.ext import commands
import os
import asyncio
import io
import importlib
import requests


global client
client = commands.Bot(command_prefix = 'a!')


@client.command()
async def image(ctx):

    data=requests.get(ctx.message.attachments[0].url).content
    data_bytes = io.BytesIO(data)

    await ctx.channel.send(file=discord.File(data_bytes, ctx.message.attachments[0].filename))

    await ctx.message.delete()



### ON BOT Ready
@client.event
async def on_ready():
    print("bot cheese")



#BOT start
client.run('OTUzMzAwMjE0ODM4NTk5NzEx.YjCkAg.9r030zDOrIx38EOZndKZ4AZl1Vg')
