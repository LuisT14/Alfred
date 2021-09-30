# Abstract class used to make bot events/modules
class BotEvent:
    def __init__(self):

        # Alias are is a dictionary that containes information of the commands 
        # Format {alies : command}
        # Ex {'p': 'PLAY', 'play': 'PLAY', 's' : 'STOP'}
        self.alias = {}

        # Whether commands are cap sensitve
        self.CapsMatter = True


    # Takes command Name, and data to perform action
    def parseAction(self, commandName: str, data:str, discordMSGOBJ):
        actionMethod = getattr(self, commandName)
        actionMethod(data, discordMSGOBJ)
