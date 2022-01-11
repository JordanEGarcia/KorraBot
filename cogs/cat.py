import json;
import requests
import discord
from discord.ext import commands

class Cat(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print("nya")
    
    #commands
    @commands.command()
    async def nya(self, ctx):
        await ctx.send("did someone say nya nya?! ")
        await ctx.send(cat_Images())

def setup(client):
    """ Setup Cat Module"""
    client.add_cog(Cat(client))

def cat_Images():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = json.loads(response.text)
    cat_image = json_data[0]["url"]
    return cat_image