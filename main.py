import discord;
from discord.ext import commands
import os;
import json;

listener = discord.Client()
client = commands.Bot(command_prefix = 'nya ')
    
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Messing with your favorite librarian~ | nya help"))

@client.event
async def on_message(message):
    await client.wait_until_ready()
    channel = client.get_channel(877360429951778837) # are you sure this channel exists?
    if message.channel == message.author.dm_channel: # do not use guild == None, as group dms might satisfy this, and you can't message yourself, no need to check client user
        embed = discord.Embed(
            title = 'Support requested!',
            description = f'{message.content}',
            color = 0x9fffff
            )
        embed.set_footer(text=f'Requested by {message.author.display_name} | ID-{message.author.id}')
        await channel.send(embed=embed)
        print("Support requested by {} | ID-{}!" .format(message.author, message.author.id))
        print("Content: '{}'." .format(message.content))
    await client.process_commands(message)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print(filename)
        client.load_extension(f'cogs.{filename[:-3]}')

with open('secrets.json') as filename:
    secret = json.load(filename)

client.run(secret["discordAPI"])
