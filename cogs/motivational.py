import json;
import requests
import discord
from discord.ext import commands
import random

class Motivational(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        if any(word in message.content for word in sad_words):
            await message.channel.send(random.choice(starter_encourougements))
    #commands
    @commands.command()
    async def quote(self, ctx):
        await ctx.send(get_quote())

def setup(client):
    """ Setup Cat Module"""
    client.add_cog(Motivational(client))

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n - ME"
    return quote

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encourougements = [
"*pat pat*"
"Cheer up! I believe in you!",
"Who cares",
"Remember you are special there is no one like you out there.",
"I had days like those too. I'm not good very good with words but maybe <@201184088118394880> can help?"
]