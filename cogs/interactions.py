import json;
import requests
import discord
from discord.ext import commands
import random

class Interactions(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client
    #events
    @commands.Cog.listener()
    async def on_ready(self):
        return
    
def setup(client):
    """ Setup Cat Module"""
    client.add_cog(Interactions(client))