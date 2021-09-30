import discord
from discord import channel 
from app.discordHandler.parsing import *

PREFIX = '-'


class discordClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_mesage(self, message):
        
        # ignore messages from Alfred
        if message.author == self.user:
            return


        # parse what kind of command 
        mode, text = botCommandParse(message, PREFIX)


        # if not a command
        if mode == -1:
            return


        # if Music command
        if mode == 'p':


       