import discord
import youtube_dl
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client
        #events
    @commands.Cog.listener()
    async def on_ready(self):
        return
    #commands
    """
    Connect to Voice
    If no one is in the voice channel dont do anything
    """
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
    
    """
    Disconnect From voice
    """
    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
    
    """
    Play that funky music
    """
    @commands.command()
    async def play(self, ctx, url):

        with youtube_dl.YoutubeDL({'format':"bestaudio"}) as ydl:
            ydl.cache.remove()
            info = ydl.extract_info(url,download=False)
            url2 = info['formats'][0]['url']
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url2))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

def setup(client):
    """ Setup music Module"""
    client.add_cog(Music(client))
