import json;
import requests
import discord
import os
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
        await ctx.send("Did someone say nya nya?! ")
        await ctx.send(cat_Images())
    @commands.command()
    async def cat(self, ctx):
        await ctx.send(nya_giphy())

def setup(client):
    """ Setup Cat Module"""
    client.add_cog(Cat(client))

def cat_Images():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = json.loads(response.text)
    cat_image = json_data[0]["url"]
    return cat_image

def nya_giphy():
    with open('secrets.json') as filename:
        secret = json.load(filename)
    url = "https://api.giphy.com/v1/gifs/search?api_key=" + secret["giphyAPI"] + "&limit=1&q=nyancat"
    response = requests.get("https://api.giphy.com/v1/gifs/search?api_key=" + secret["giphyAPI"] + "&limit=1&q=nyancat")
    json_data = json.loads(response.text)
    print(url)
    return json_data["data"][0]["url"]