import json
from discord.ext.commands import context
from discord.ext.commands.core import command;
import requests
import discord
from discord.ext import commands
import random
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_random_response
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Interactions(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client
    #events
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot, self.trainer = turnOnBot()
        return
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        else:
            if self.client.user.mentioned_in(message):
                notclean, clean = message.content.split(">")
                await message.channel.send(botResponse(self.bot, clean[1:]))
                print(clean[1:])
    
    @commands.command()
    async def hug(self,ctx):
        saveBot(self.trainer)
        await ctx.send()

def setup(client):
    """ Setup Cat Module"""
    client.add_cog(Interactions(client))


def turnOnBot():
    my_bot = ChatBot(
        'Korra',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                "statement_comparison_function": LevenshteinDistance,
                "response_selection_method": get_random_response
            }
        ]
    )
    list_trainer = ListTrainer(my_bot)

    trainer = ChatterBotCorpusTrainer(my_bot)
    trainer.train('chatterbot.corpus.english', "./db/chatbot/")
    return [my_bot, trainer]

def botResponse(bot, input):
    return (bot.get_response(input));

def saveBot(trainer):
    trainer.export_for_training('./my_export.json')