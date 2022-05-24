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
    @commands.command(brief='I hug you', description='I am hugging you what more can you ask for!')
    async def hug(self, ctx):
        await ctx.send("hugs " +  ctx.author.name  + " back!")

    @commands.command(brief='just a lick :D', description='I am licking you. what more can you ask for!')
    async def lick(self,ctx):
    	await ctx.send("licks " +  ctx.author.name + " back")

    @commands.command(brief='Flip a Korra', description="It's like flipping a coin, but a bit better")
    async def flip(self,ctx):
    	await ctx.send("Flips a coin and...\n\n " + random.choice(["... lays on my back. Y-you can touch my tail", "...fidgets a little. I-I guess you can pet my head.", "...grabs it! Don't look at me like that. I need the money!", "...headbutts you! OWW! You've got such a hard head!", "...pins the tail on my little donkey... I MEAN YOU, YA DUTZ!", "...the coin keeps flipping and flipping and flipping and flipping and flipping and flipping...", "...shaves off all of your hair. Nya hahaha!", "...slaps you on the tooshie! Ji ji ji ji", "...lands on the edge! WOAH!", "...curls up on the top of your head. Yaaawn. What a good napping face.", "...booty bumps ya!", "...hands your a brush. Go ahead and brush my tail, why dontcha?"]))

    @commands.command(brief="I'm warning you, just dont...", description="I will get angry and use my fullest authority to bring you down.")
    async def horny(self, ctx):
    	await ctx.send("https://i.gifer.com/5Dy.gif")
    	await ctx.send("GO TO BRAZIL! \n "+ ctx.author.mention  + " is dead...")

    @commands.command()
    async def propose(self,ctx):
    	await ctx.send("You have to be at least as rich as me to propose!")
    @commands.command(brief="nya roll 25", description="Roll a number of you choosing. Or be default of 6.")
    async def roll(self,ctx, url=6):
        if (isinstance(url, int)):
            random_value = str(random.randrange(url)+1)
            await ctx.send(ctx.author.name + " rolled a " + random_value + ". Nya!")
            if (random_value == "1"):
                await ctx.send("oof...")
        else:
            await ctx.send("Use a real number, dum dum.")
    @commands.command(brief="Wha... but why...", description="Kiss me and you'll be having a hard time")
    async def kiss(self,ctx):
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
