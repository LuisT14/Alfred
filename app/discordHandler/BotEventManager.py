# To manage all Bot events and direct information to bot Events
from app.discordHandler.BotEvent import BotEvent

class BotEventManager:
    def __init__(self, listOfBotEvents: list, prefix: str):

        self.botEventList = []
        self.prefix = prefix
        # Check if every item is BotEvent
        for item in list:
            if(not issubclass(BotEvent, item)):
                continue
            self.botEventList.append(item)

    def commandProcess(self, text: str, discordMessageObject):
        if text[0] != self.prefix:
            return False

        aliesC = text[1::].split(" ")[0]

        for botEventC in self.botEventList:        
            if aliesC in botEventC.alias:
                botEventC.parseAction(botEventC.alias[aliesC], text[len(aliesC)::], discordMessageObject)
                return True
        
        return False

