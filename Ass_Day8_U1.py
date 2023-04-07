from email.mime import image
import discord
from discord.ext import commands
import time
import os
import random

TOKEN ='MTAxMTg0NzQwNTQ1NDQ5OTg5MA.GhVtMc.9PNjyTIRuEYEKd-VVxEdCdcc4QySbVX3JqdRqA'

intent = discord.Intents.default()
intent.members = True

client = commands.Bot(command_prefix='!', intents=intent)

channelID = 1011838444290445376
channel = client.get_channel(channelID)

@client.event
async def on_ready():
    print('Bot is NOW')
    print('------------')
    channel = client.get_channel(1011838444290445376)
    await channel.send('Hi, I am bot')
    while True:
        await channel.send(file=discord.File('Cat/'+random.choice(images)))
        time.sleep(5)
    
client.run(TOKEN)
