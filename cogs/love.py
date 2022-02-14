import json;
import requests
import discord
from discord.ext import commands
import random
from PIL import Image
from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageDraw
class Love(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        return
    @commands.command()
    async def hug(self, ctx):
        await ctx.send("hugs " +  ctx.author.name  + " back!")
    @commands.command()
    async def kiss(self,ctx):
    	await ctx.send("kisses " + ctx.author.name + " back!")
    @commands.command()
    async def lick(self,ctx):
    	await ctx.send("licks " +  ctx.author.name + " back")
    @commands.command()
    async def flip(self,ctx):
    	await ctx.send("Flips a coin and lays on my back...\n\n " + random.choice(["... you can touch my tail", "...you can pet my head"]))
    @commands.command()
    async def horny(self, ctx):
    	await ctx.send("https://i.gifer.com/5Dy.gif")
    	await ctx.send("GO TO BRAZIL! \n "+ ctx.author.mention  + " is dead...")
    @commands.command()
    async def propose(self,ctx):
    	await ctx.send("You have to be at least as rich as me to propose!")
    @commands.command()
    async def wanted(self,ctx):
        wanted = Image.open("db/images/wanted.jpg")
        asset = ctx.author.avatar_url_as(size = 128)
        draw = ImageDraw.Draw(wanted)
        font = ImageFont.truetype("db/fonts/Palatino.tff", 40)
        draw.text((61,310), ctx.author.name[0:9] ,(0,0,0),font=font)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((180,180))
        wanted.paste(pfp, (67,89))
        wanted.save("profile.jpg")
        await ctx.send("*HISSSSSSSS* Someone kissed me without my permission! \n Everyone find this person and get them!")
        await ctx.send(file = discord.File("profile.jpg"))
def setup(client):
    """ Setup Cat Module"""
    client.add_cog(Love(client));