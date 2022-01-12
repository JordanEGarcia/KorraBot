import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client
        #events
    @commands.Cog.listener()
    async def on_ready(self):
        print("nya")
    #commands
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Please join a voice channel. I get lonely if i Listen to music by myself...")
        else:
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)
    
    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

def setup(client):
    """ Setup music Module"""
    client.add_cog(Music(client))
