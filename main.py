import discord;
from discord.ext import commands
import os;
import requests;
import random
import schedule

listener = discord.Client()
client = commands.Bot(command_prefix = 'nya ')
    
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Messing with your favorite librarian~ | nya help"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print(filename)
        client.load_extension(f'cogs.{filename[:-3]}')

client.run((os.getenv('TOKEN')))