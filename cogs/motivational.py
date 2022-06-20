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
        if "wrong answer" in message.content:
            await message.channel.send("https://media.discordapp.net/attachments/872277715112317011/961280245384773632/korra_with_a_gun.png?width=702&height=702")
        if any(word in message.content for word in sad_words):
            await message.channel.send(random.choice(starter_encourougements))
    #commands
    @commands.command()
    async def quote(self, ctx):
        await ctx.send(get_quote())

    @commands.command()
    async def advice(self, ctx):
        await ctx.send(get_advice())

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        else:
            if self.client.user.mentioned_in(message):
                notclean, clean = message.content.split(">")
                await message.channel.send(requests.get(f'http://localhost:8000/request?input={(clean[1:])}').text)
                
def setup(client):
    """ Setup Cat Module"""
    client.add_cog(Motivational(client))

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n - ME"
    return quote

def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    json_data = json.loads(response.text)
    advice = json_data["slip"]['advice']
    return advice

sad_words = [" sad ", "depressed", "unhappy", "angry", "miserable", "depressing", " cry "]
starter_encourougements = [
"I'm here for you. Cry if you need to",
"I promise it will get better, maybe not now, but one day",
"I can go shopping with you later if that'll make you feel better?",
"I'll be there to cheer you up. Give me a bit."
"https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif",
"*pat pat*",
"Cheer up! I believe in you!",
"Who cares",
"Remember you are special there is no one like you out there.",
"I had days like those too. I'm not good very good with words but maybe <@201184088118394880> can help?"

]
