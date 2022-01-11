import discord;
import os;
import requests;
import json;
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encourougements = [
"*pat pat*"
"Cheer up! I believe in you!",
"Who cares",
"Remember you are special there is no one like you out there.",
"I had days like those too. I'm not good very good with words but maybe <@201184088118394880> can help?"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - Korra"
    return quote

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(starter_encourougements))

client.run((os.getenv('TOKEN')))