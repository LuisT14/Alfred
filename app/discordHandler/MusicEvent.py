from asyncio.queues import Queue
from discord import message
from discord.enums import try_enum
from app.discordHandler.BotEvent import BotEvent
from discord import channel
import discord
import os
from discord import voice_client
import threading 

class MusicEvent(BotEvent):

    def __init__(self):
        self.alias = {'p' : 'PLAY', 'play' : 'PLAY', 'skip' : 'SKIP', 's' : 'SKIP', 'pt': 'PLAYTOP', 'playtop' : 'PLAYTOP', 'j': 'JOIN', 'join' : 'JOIN',  'pause' : 'PAUSE', 'ps': 'PLAYSKIP' , 'playskip' : 'PLAYSKIP', 'leave': 'LEAVE' , 'fuckoff' : 'LEAVE', 'np' : 'NOWPLAYING', 'nowplaying' : 'NOWPLAYING', 'q' : 'QUEUE' , 'queue' : 'QUEUE' , 'rm' : 'REMOVE', 'remove' : 'REMOVE', 'clear' : 'CLEAR'}
        self.CapsMatter = False
        self.joined = False
        self.queue = []
        self.vcI = None

    def QueueCheck(self):
        while len(self.queue) != 0:
            if not self.vcI.is_playing():
                pass

    def createQueueThread(self):
        self.QueueThread = threading.Thread(target=self.QueueCheck)




    def CheckVC(dMessageObj: discord.Message):
        if dMessageObj.author.voice.channel:
            return True
        else:
            return False

    async def PLAY(self, data, dMessageObj: discord.Message):
        if not self.joined:
            if not self.CheckVC:
                await dMessageObj.channel.send("Connect to a Voice Channel First")
                return
            self.joined = True
            self.vcI = dMessageObj.author.voice.channel.connect()
        
        if len(self.queue)  == 0 and  not self.vcI.is_playing():
            self.vcI.play
            return 

        if len(self.queue)  == 0 and self.vcI.is_playing():
            self.queue.append(data)


        self.queue.append(data)

