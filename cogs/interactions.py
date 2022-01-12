import json;
import requests
import discord
from discord.ext import commands
import random

class Interactions(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client
