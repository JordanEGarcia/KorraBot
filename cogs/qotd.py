import discord
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from discord.ext import commands
from discord.ext import tasks

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://leafy-tuner-238701-default-rtdb.firebaseio.com/'})

################################
#
# Function: process the newest questions and send it back to the qotd class
#
###############################
def post(self):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    handle = db.reference('Question')
    question = handle.order_by_key().get()
    embed = discord.Embed(
        title = '❔❓ Question of the day! ❔❓',
        description = f' Question:  {list(question.items())[0][1]} ',
        color = 0x9fffff
        )
    embed.set_footer(text=f' Asked by: Korra! • {len(question)} Questions Left • Today at {current_time}')
    db.reference(f"Question/{list(question.items())[0][0]}").delete()
    return embed


class qotd(commands.Cog):
    def __init__(self, client):
        """ Initialize Cat Class"""
        self.client = client
        self.channel = 876669480934191164
        self.on_ready.start()

    ################################
    #
    # Function: Reads a Question
    #
    ###############################
    @commands.command(brief='Reads a Question', description="Lists all the questions.")
    @commands.has_any_role("🌺 Front Desk🌺","🐦Calvary 🐦", 492212595072434186, 971578555551088740)
    async def q_read(self,ctx):
        handle = db.reference('Question')
        question = handle.order_by_key().get()
        await ctx.send(f'The next Question is going to be: {question[0]}.')
        await ctx.send(" All of them can be read here: https://console.firebase.google.com/u/0/project/leafy-tuner-238701/database/leafy-tuner-238701-default-rtdb/data")
        await ctx.send(f'{len(question)} questions left. Please add more.')

    ################################
    #
    # Function: Add a Question
    #
    ###############################
    @commands.command(brief='Add A Question', description="Add a question to the question of the day.")
    @commands.has_any_role("🌺 Front Desk🌺","🐦Calvary 🐦", 492212595072434186, 971578555551088740)
    async def q_add(self,ctx, question):
        handle = db.reference('Question')
        handle.push(question)
        await ctx.send("Question Sent successfully thank you!")
    
    ################################
    #
    # Function: Posts a Question
    #
    ###############################
    @commands.command(brief='Post A Question', description="Post a question to the question of the day.")
    @commands.has_any_role("🌺 Front Desk🌺","🐦Calvary 🐦", 492212595072434186, 971578555551088740)
    async def q_post(self,ctx):
        print("making a post")
        channel = self.client.get_channel(self.channel)
        await channel.send(embed=post(self))

    ################################
    #
    # Question Of The Day Timer
    # When the time is ##:## post the question 
    #
    ###############################
    @tasks.loop(hours=1) 
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        current_time = datetime.now().strftime("%H")
        print(current_time)
        # When the time is ##:## start the stuff!
        if(current_time == '9'):
            channel = self.client.get_channel(self.channel)
            await channel.send(embed=post(self))

def setup(client):
    """ Setup Cat Module"""
    client.add_cog(qotd(client))


